"""
split_by_subtopic.py
--------------------
Splits a large PDF into per-depth-1-topic PDFs, preserving bookmarks.

Rules:
- Only depth-1 bookmarks become output PDFs
- Skip depth-0 bookmarks (doc title wrappers)
- Skip Table of Contents bookmarks
- Skip pure container bookmarks (first child on same page)
- Each output PDF contains all pages for that topic
- Bookmarks from the original PDF that fall within each topic's page
  range are copied into the output PDF with remapped page numbers
- OVERLAP: shared boundary page appears in both adjacent PDFs
- Output: subtopic_pdfs/{input_name}/{order:03d}_d1_{slug}.pdf

Requirements:
    pip install pikepdf pypdf
"""

import os
import re
import sys
import pikepdf
from pypdf import PdfReader, PdfWriter

# ── Set your PDF path here ────────────────────────────────────────────────────
INPUT_PDF = r"C:\Users\shesh\PycharmProjects\pdf doc split\servicenow-australia-governance-risk-compliance-enus.pdf"
# ─────────────────────────────────────────────────────────────────────────────

SKIP_TITLES = {"table of contents", "toc"}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "_", text)
    return text[:80] or "untitled"


def build_page_index(pdf):
    idx = {}
    for i, p in enumerate(pdf.pages):
        try:
            idx[p.obj.objgen] = i
        except Exception:
            pass
    return idx


def resolve_named_dests(pdf):
    named = {}
    root = pdf.Root
    if "/Names" in root and "/Dests" in root.Names:
        def _walk(node):
            if "/Names" in node:
                arr = node.Names
                for j in range(0, len(arr) - 1, 2):
                    named[str(arr[j])] = arr[j + 1]
            if "/Kids" in node:
                for kid in node.Kids:
                    _walk(kid)
        _walk(root.Names.Dests)
    if "/Dests" in root:
        for k in root.Dests.keys():
            named[str(k)] = root.Dests[k]
    return named


def dest_to_page(item, page_index, named_dests):
    obj = item.obj
    dest = None
    if "/Dest" in obj:
        dest = obj.Dest
    elif "/A" in obj and "/D" in obj.A:
        dest = obj.A.D
    if dest is None:
        return None
    if isinstance(dest, (pikepdf.String, pikepdf.Name)):
        dest = named_dests.get(str(dest))
        if dest is None:
            return None
    if isinstance(dest, pikepdf.Dictionary) and "/D" in dest:
        dest = dest.D
    if isinstance(dest, pikepdf.Array) and len(dest) > 0:
        try:
            return page_index.get(dest[0].objgen)
        except Exception:
            return None
    return None


def flatten_outline(pdf):
    page_index  = build_page_index(pdf)
    named_dests = resolve_named_dests(pdf)
    flat = []

    def walk(items, depth):
        for item in items:
            title = str(item.title).strip() if item.title else ""
            page  = dest_to_page(item, page_index, named_dests)
            flat.append((depth, title, page))
            if item.children:
                walk(item.children, depth + 1)

    with pdf.open_outline() as outline:
        walk(outline.root, 0)
    return flat


def compute_depth1_sections(flat, total_pages):
    """Returns list of (title, page_list) for depth-1 topics only."""
    valid = [(d, t, p) for d, t, p in flat if p is not None]

    skip_pages = set()
    for i, (d, t, p) in enumerate(valid):
        if t.lower() in SKIP_TITLES:
            end = total_pages
            for j in range(i + 1, len(valid)):
                if valid[j][0] <= d:
                    end = valid[j][2]
                    break
            skip_pages.update(range(p, end))

    def get_next_start(i, depth):
        """Returns the 0-indexed page where the next sibling/parent starts, or None."""
        for j in range(i + 1, len(valid)):
            if valid[j][0] <= depth:
                return valid[j][2]
        return None

    sections = []
    for i, (d, t, p) in enumerate(valid):
        if t.lower() in SKIP_TITLES:
            continue
        if d == 0:
            continue
        if d > 1:
            continue
        # Container check removed — at depth-1 every topic becomes its own PDF
        next_start = get_next_start(i, d)

        if next_start is None:
            # Last section — goes to end of document
            end_exclusive = total_pages
        else:
            # Overlap rule: include the boundary page in THIS section too,
            # because the previous topic may end mid-page where the next begins.
            # end_exclusive is next_start + 1 so the boundary page is included.
            end_exclusive = next_start + 1

        pages = [pg for pg in range(p, end_exclusive) if pg not in skip_pages]
        if pages:
            sections.append((t, pages))

    return sections


def copy_bookmarks_for_range(src_pdf, flat, page_range_set,
                             dst_pdf, page_map):
    """
    Copy all bookmarks from src_pdf whose target page is within
    page_range_set into dst_pdf, remapping page numbers via page_map
    (src_page_0indexed -> dst_page_0indexed).
    Rebuilds the full nested outline structure.
    """
    page_index  = build_page_index(src_pdf)
    named_dests = resolve_named_dests(src_pdf)

    def walk_and_copy(src_items, dst_parent):
        for item in src_items:
            title    = str(item.title).strip() if item.title else ""
            src_page = dest_to_page(item, page_index, named_dests)

            if src_page is not None and src_page in page_range_set:
                dst_page = page_map[src_page]
                node     = pikepdf.OutlineItem(title)
                node.destination = pikepdf.Array([
                    dst_pdf.pages[dst_page].obj,
                    pikepdf.Name.Fit
                ])
                dst_parent.append(node)
                # Recurse into children
                if item.children:
                    walk_and_copy(item.children, node.children)
            else:
                # Even if this item is out of range, its children might be in range
                if item.children:
                    walk_and_copy(item.children, dst_parent)

    with src_pdf.open_outline() as src_outline:
        with dst_pdf.open_outline() as dst_outline:
            walk_and_copy(src_outline.root, dst_outline.root)


def main(input_pdf):
    if not os.path.isfile(input_pdf):
        print(f"File not found: {input_pdf}")
        sys.exit(1)

    base_name  = os.path.splitext(os.path.basename(input_pdf))[0]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir    = os.path.join(script_dir, "subtopic_pdfs", base_name)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\nInput  : {input_pdf}")
    print(f"Output : {out_dir}\n")

    # Open with pikepdf for bookmark work
    src_pikepdf = pikepdf.open(input_pdf)
    total       = len(src_pikepdf.pages)
    flat        = flatten_outline(src_pikepdf)

    print(f"Total pages : {total}")
    print(f"Bookmarks   : {len(flat)}")

    sections = compute_depth1_sections(flat, total)
    print(f"Subtopics   : {len(sections)}\n")

    for order, (title, page_list) in enumerate(sections, start=1):
        fname    = f"{order:03d}_d1_{slugify(title)}.pdf"
        out_path = os.path.join(out_dir, fname)

        page_range_set = set(page_list)
        # page_map: original page index -> new local index
        page_map = {orig: local for local, orig in enumerate(page_list)}

        # Build the output PDF with pikepdf so we can attach bookmarks
        dst = pikepdf.new()
        for pg in page_list:
            dst.pages.append(src_pikepdf.pages[pg])

        # Copy and remap bookmarks
        copy_bookmarks_for_range(
            src_pikepdf, flat, page_range_set, dst, page_map
        )

        dst.remove_unreferenced_resources()
        dst.save(out_path, compress_streams=True)
        dst.close()

        size_kb = os.path.getsize(out_path) // 1024
        print(f"  {order:03d}. '{title}'")
        print(f"       → {fname}  "
              f"({len(page_list)} pages, "
              f"p{page_list[0]+1}–{page_list[-1]+1}, "
              f"{size_kb} KB)")

    src_pikepdf.close()
    print(f"\nDone — {len(sections)} PDFs saved to:\n  {out_dir}")


if __name__ == "__main__":
    main(INPUT_PDF)