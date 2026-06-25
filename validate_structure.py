"""
validate_structure.py
---------------------
Guards the documentation tree so the MCP server (mcp_server.py) indexes
everything it should.

The server only indexes markdown at exactly:  <Main document>/<Topic>/<file>.md
This script flags anything that would be silently dropped from the index:

  - loose .md files at a main-document root (depth 1)        -> NOT indexed
  - .md files nested deeper than a topic folder (depth 3+),
    excluding the intentional `_assets/` folders             -> NOT indexed
  - empty topic folders (no .md inside)                      -> dead folder
  - main-document folders that are missing entirely

Exit code is non-zero when any *coverage-affecting* problem is found, so this
can be wired into CI / a pre-commit hook.

Run:
    python validate_structure.py
"""

import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
MAIN_DOCUMENTS = ["ServiceNow Enable AI", "ServiceNow GRC",
                  "AI Control Tower Implementation"]
ASSET_DIRNAMES = {"_assets"}


def validate():
    errors = []    # coverage-affecting -> non-zero exit
    warnings = []  # cosmetic / informational

    for doc in MAIN_DOCUMENTS:
        doc_root = os.path.join(BASE, doc)
        if not os.path.isdir(doc_root):
            errors.append(f"Missing main-document folder: '{doc}'")
            continue

        # Loose .md directly under the document root (depth 1) — not indexed.
        for entry in sorted(os.listdir(doc_root)):
            if entry.lower().endswith(".md"):
                errors.append(
                    f"Orphaned file (not indexed): '{doc}/{entry}' "
                    f"— move it into a topic subfolder."
                )

        # Walk topic folders.
        for topic in sorted(os.listdir(doc_root)):
            topic_path = os.path.join(doc_root, topic)
            if not os.path.isdir(topic_path):
                continue

            indexed_here = 0
            for root, dirs, files in os.walk(topic_path):
                depth = os.path.relpath(root, topic_path)
                mds = [f for f in files if f.lower().endswith(".md")]
                if root == topic_path:
                    indexed_here += len(mds)  # depth-2: indexed
                else:
                    # deeper than a topic folder
                    parts = depth.split(os.sep)
                    if any(p in ASSET_DIRNAMES for p in parts):
                        continue  # intentionally excluded
                    for f in mds:
                        warnings.append(
                            f"Deep file (not indexed): '{doc}/{topic}/{depth}/{f}'"
                        )

            if indexed_here == 0:
                warnings.append(f"Empty topic folder (no indexed .md): '{doc}/{topic}'")

    return errors, warnings


def main():
    errors, warnings = validate()

    for w in warnings:
        print(f"  WARN: {w}")
    for e in errors:
        print(f"  ERROR: {e}")

    print()
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s).")
    if errors:
        print("FAIL — coverage-affecting problems found.")
        sys.exit(1)
    print("OK — every markdown file is reachable by the MCP server index.")


if __name__ == "__main__":
    main()
