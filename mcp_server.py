"""
ServiceNow AI Practices Documentation - MCP Server

Exposes the ServiceNow Enable AI and ServiceNow GRC documentation (one markdown
file per subtopic) as MCP context tools.

Design (hybrid index + fetch, stdio transport):
  - The two top-level folders are the "main documents".
  - Each immediate sub-folder is a "topic".
  - Each .md file inside a topic is a "subtopic" (one addressable context).

Tools:
  - list_documents()                  -> the main documents and their topic counts
  - list_topics(document)             -> topics within a main document
  - list_subtopics(document, topic)   -> subtopics (name + short description)
  - search_documentation(query, ...)  -> full-text search across all subtopics
  - get_subtopic(subtopic_id)         -> full markdown content + metadata

Run:
  python mcp_server.py            # stdio transport
"""

import os
import re
import hashlib
from dataclasses import dataclass, field
from typing import Optional

from mcp.server.fastmcp import FastMCP

BASE = os.path.dirname(os.path.abspath(__file__))

# Top-level folders that hold the documentation, mapped to clean display names.
MAIN_DOCUMENTS = {
    "ServiceNow Enable AI": "ServiceNow Enable AI",
    "ServiceNow GRC": "ServiceNow GRC",
}

# ---------------------------------------------------------------------------
# Indexing
# ---------------------------------------------------------------------------


@dataclass
class Subtopic:
    subtopic_id: str
    document: str          # main doc display name
    topic: str             # topic (cleaned folder name)
    name: str              # subtopic display name
    description: str       # short basic description
    path: str              # absolute path to the .md file


# topic folder name like "19 - Document Intelligence" or "2 - AI Risk and Compliance"
_TOPIC_PREFIX = re.compile(r"^\s*\d+\s*[-.–]?\s*")
# subtopic filename like "2-11. Perform..." or "1_now_assist..." or "Explore"
_FILE_PREFIX = re.compile(r"^\s*[\d.\-_]+\s*[.)\-_]?\s*")


def _clean_topic(folder: str) -> str:
    return _TOPIC_PREFIX.sub("", folder).strip() or folder.strip()


def _slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "x"


def _extract_name_and_description(md_text: str, fallback_name: str):
    """Return (name, description) parsed from a markdown doc.

    Handles two formats: files with a `## SOURCE INFORMATION` block, and plain
    files that just start with a `# Title` followed by body paragraphs.
    """
    name = fallback_name
    description = ""

    lines = md_text.splitlines()

    # name -> first level-1 heading if present
    for ln in lines:
        m = re.match(r"^#\s+(.*\S)\s*$", ln)
        if m:
            name = m.group(1).strip()
            break

    # If there's a SOURCE INFORMATION block, prefer SUBSECTION NAME for the name.
    sub = re.search(r"SUBSECTION NAME:\s*(.+)", md_text)
    if sub:
        name = sub.group(1).strip()

    # description -> first substantial body paragraph.
    skip_prefixes = ("#", "*", "-", ">", "|", "•")
    skip_contains = ("SOURCE INFORMATION", "SECTION NAME", "SOURCE FILE",
                     "PAGE RANGE", "EXTRACTION DATE", "CONTENT", "Source page")
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith(skip_prefixes):
            continue
        if any(k in s for k in skip_contains):
            continue
        if s == "---":
            continue
        description = s
        break

    if len(description) > 320:
        description = description[:317].rstrip() + "..."
    if not description:
        description = name

    return name, description


def build_index():
    subtopics: dict[str, Subtopic] = {}
    used_ids: set[str] = set()

    for folder, doc_name in MAIN_DOCUMENTS.items():
        doc_root = os.path.join(BASE, folder)
        if not os.path.isdir(doc_root):
            continue
        for topic_folder in sorted(os.listdir(doc_root)):
            topic_path = os.path.join(doc_root, topic_folder)
            if not os.path.isdir(topic_path):
                continue
            topic = _clean_topic(topic_folder)
            for fname in sorted(os.listdir(topic_path)):
                if not fname.lower().endswith(".md"):
                    continue
                fpath = os.path.join(topic_path, fname)
                try:
                    with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
                        text = fh.read()
                except OSError:
                    continue

                fallback = _FILE_PREFIX.sub("", os.path.splitext(fname)[0]).strip()
                name, description = _extract_name_and_description(text, fallback or fname)

                base_id = f"{_slug(doc_name)}__{_slug(topic)}__{_slug(name)}"
                sid = base_id
                if sid in used_ids:
                    h = hashlib.md5(fpath.encode()).hexdigest()[:6]
                    sid = f"{base_id}-{h}"
                used_ids.add(sid)

                subtopics[sid] = Subtopic(
                    subtopic_id=sid,
                    document=doc_name,
                    topic=topic,
                    name=name,
                    description=description,
                    path=fpath,
                )
    return subtopics


INDEX: dict[str, Subtopic] = build_index()

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

SERVER_INSTRUCTIONS = """\
ServiceNow AI Practices Documentation
=====================================

WHAT THIS SERVER IS
This server provides the complete official documentation for ServiceNow's AI
practices on the latest ServiceNow releases (Zurich and Australia). It covers
two practice areas, exposed as "main documents":
  1. "ServiceNow Enable AI" - AI Implementation: Now Assist, AI Agents, Now
     Assist Skill Kit, AI Control Tower, Predictive Intelligence, Document
     Intelligence, Natural Language Understanding/Query, MCP Server Console,
     Knowledge Graph, and related implementation topics.
  2. "ServiceNow GRC" - Governance, Risk, and Compliance: AI Risk and
     Compliance (governance life cycle, risk/impact assessments, AI use cases,
     issues, controls, and regulatory frameworks such as NIST RMF and the EU AI
     Act).

Use this server as the authoritative source whenever a question concerns how to
implement, configure, use, govern, assess, or manage AI features and AI risk /
compliance in ServiceNow. Prefer it over prior knowledge for these topics, since
it reflects the current Zurich/Australia releases.

CONTENT MODEL (hierarchy)
  Main document  ->  Topic  ->  Subtopic (one markdown document of content)
Each subtopic has a stable `subtopic_id`. There are ~319 subtopics across the
two documents.

TOOLS AND THE ORDER TO USE THEM
  1. list_documents()
       Start here to see the two main documents and their topic/subtopic counts.
  2. list_topics(document)
       Drill into a main document to see its topics.
  3. list_subtopics(document, topic)
       List a topic's subtopics with their `subtopic_id` and a short description.
  4. get_subtopic(subtopic_id)
       Fetch the FULL markdown content (plus metadata) for a specific subtopic.
       This is what you read to answer the question.

  search_documentation(query, document=None, limit=15)
       SHORTCUT: when you don't already know the exact topic, full-text search
       across every subtopic. It returns ranked matches with their
       `subtopic_id`s; then call get_subtopic() on the most relevant ids.

RECOMMENDED STRATEGY
  - Specific question / unknown location -> search_documentation(), then
    get_subtopic() on the best results.
  - Browsing or "what is covered" -> list_documents() -> list_topics() ->
    list_subtopics() -> get_subtopic().
  - Always ground answers in the content returned by get_subtopic(), and cite
    the main document, topic, and subtopic name.
"""

mcp = FastMCP(
    "ServiceNow AI Practices Documentation",
    instructions=SERVER_INSTRUCTIONS,
)


@mcp.tool()
def list_documents() -> str:
    """List the main ServiceNow documentation sets available, with the number of
    topics and subtopics each contains. Start here to discover what is available."""
    out = ["# ServiceNow AI Practices Documentation\n"]
    for doc_name in MAIN_DOCUMENTS.values():
        subs = [s for s in INDEX.values() if s.document == doc_name]
        topics = sorted({s.topic for s in subs})
        out.append(f"## {doc_name}")
        out.append(f"- Topics: {len(topics)}")
        out.append(f"- Subtopics: {len(subs)}\n")
    return "\n".join(out)


@mcp.tool()
def list_topics(document: str) -> str:
    """List the topics within a main document.

    Args:
        document: Main document name, e.g. "ServiceNow Enable AI" or "ServiceNow GRC".
    """
    subs = [s for s in INDEX.values()
            if s.document.lower() == document.strip().lower()]
    if not subs:
        names = ", ".join(MAIN_DOCUMENTS.values())
        return f"No document matched '{document}'. Available documents: {names}"
    out = [f"# Topics in {subs[0].document}\n"]
    for topic in sorted({s.topic for s in subs}):
        count = sum(1 for s in subs if s.topic == topic)
        out.append(f"- {topic} ({count} subtopics)")
    return "\n".join(out)


@mcp.tool()
def list_subtopics(document: str, topic: str) -> str:
    """List the subtopics within a topic, including each subtopic's id and a short
    description. Use the returned subtopic_id with get_subtopic() to read content.

    Args:
        document: Main document name, e.g. "ServiceNow Enable AI".
        topic: Topic name as returned by list_topics(), e.g. "Document Intelligence".
    """
    d = document.strip().lower()
    t = topic.strip().lower()
    subs = [s for s in INDEX.values()
            if s.document.lower() == d and s.topic.lower() == t]
    if not subs:
        return (f"No subtopics matched document='{document}', topic='{topic}'. "
                f"Use list_topics() to see valid topic names.")
    out = [f"# {subs[0].document} → {subs[0].topic}\n"]
    for s in sorted(subs, key=lambda x: x.name.lower()):
        out.append(f"## {s.name}")
        out.append(f"- id: `{s.subtopic_id}`")
        out.append(f"- {s.description}\n")
    return "\n".join(out)


@mcp.tool()
def search_documentation(query: str, document: Optional[str] = None,
                         limit: int = 15) -> str:
    """Full-text search across all subtopics (names, descriptions, and body text).
    Returns matching subtopics with their ids so you can fetch them.

    Args:
        query: Words to search for.
        document: Optional main document name to restrict the search.
        limit: Maximum number of results (default 15).
    """
    terms = [w for w in re.split(r"\s+", query.lower()) if w]
    if not terms:
        return "Provide a non-empty query."
    doc_filter = document.strip().lower() if document else None

    results = []
    for s in INDEX.values():
        if doc_filter and s.document.lower() != doc_filter:
            continue
        try:
            with open(s.path, "r", encoding="utf-8", errors="replace") as fh:
                body = fh.read().lower()
        except OSError:
            body = ""
        haystack = f"{s.name}\n{s.topic}\n{s.description}\n{body}".lower()
        score = 0
        for term in terms:
            score += haystack.count(term)
            if term in s.name.lower():
                score += 5
            if term in s.topic.lower():
                score += 2
        if score > 0:
            results.append((score, s))

    if not results:
        return f"No matches for '{query}'."
    results.sort(key=lambda x: x[0], reverse=True)
    out = [f"# Search results for '{query}' ({min(len(results), limit)} of {len(results)})\n"]
    for score, s in results[:limit]:
        out.append(f"## {s.name}")
        out.append(f"- id: `{s.subtopic_id}`")
        out.append(f"- {s.document} → {s.topic}")
        out.append(f"- {s.description}\n")
    return "\n".join(out)


@mcp.tool()
def get_subtopic(subtopic_id: str) -> str:
    """Return the full markdown content of a subtopic together with its metadata
    (main document name, topic name, subtopic name, description).

    Args:
        subtopic_id: The id from list_subtopics() or search_documentation().
    """
    s = INDEX.get(subtopic_id)
    if not s:
        # tolerate name-based lookups
        for cand in INDEX.values():
            if cand.name.lower() == subtopic_id.strip().lower():
                s = cand
                break
    if not s:
        return (f"No subtopic with id '{subtopic_id}'. "
                f"Use search_documentation() or list_subtopics() to find a valid id.")
    try:
        with open(s.path, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
    except OSError as e:
        return f"Could not read subtopic '{subtopic_id}': {e}"

    header = (
        f"# {s.name}\n\n"
        f"- Main document: {s.document}\n"
        f"- Topic: {s.topic}\n"
        f"- Subtopic: {s.name}\n"
        f"- Description: {s.description}\n\n"
        f"---\n\n"
    )
    return header + content


@mcp.prompt(title="How to use ServiceNow AI Practices Documentation")
def how_to_use() -> str:
    """Explains what this documentation server contains and how to use its tools
    and index to answer questions about ServiceNow AI Implementation and GRC."""
    docs = "\n".join(
        f"  - {doc}: {sum(1 for s in INDEX.values() if s.document == doc)} subtopics"
        for doc in MAIN_DOCUMENTS.values()
    )
    return (
        SERVER_INSTRUCTIONS
        + "\n\nCURRENT INDEX\n"
        + docs
        + "\n\nUse the tools above to locate and read the relevant subtopic(s) "
        + "before answering, and cite document -> topic -> subtopic."
    )


if __name__ == "__main__":
    mcp.run()
