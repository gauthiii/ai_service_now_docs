import math
import os
import pikepdf

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT_PDF = os.path.join(BASE, "servicenow_enable_ai.pdf")
PAGES_PER_CHUNK = 50
OUTPUT_DIR = os.path.join(BASE, "enable_ai_chunks")

os.makedirs(OUTPUT_DIR, exist_ok=True)

src = pikepdf.open(INPUT_PDF)
total_pages = len(src.pages)
total_chunks = math.ceil(total_pages / PAGES_PER_CHUNK)

# Map each source page object -> its index, so we can resolve bookmark targets.
page_index = {}
for i, p in enumerate(src.pages):
    page_index[p.obj.unparse()] = i  # fallback key
    try:
        page_index[(p.obj.objgen)] = i
    except Exception:
        pass

# Resolve named destinations (catalog /Names /Dests and legacy /Dests).
named_dests = {}
root = src.Root
if "/Names" in root and "/Dests" in root.Names:
    def walk_nametree(node):
        if "/Names" in node:
            arr = node.Names
            for j in range(0, len(arr), 2):
                named_dests[str(arr[j])] = arr[j + 1]
        if "/Kids" in node:
            for kid in node.Kids:
                walk_nametree(kid)
    walk_nametree(root.Names.Dests)
if "/Dests" in root:
    for k in root.Dests.keys():
        named_dests[str(k)] = root.Dests[k]


def dest_to_page_index(item):
    """Return the source page index an outline item points to, or None."""
    dest = None
    obj = item.obj
    if "/Dest" in obj:
        dest = obj.Dest
    elif "/A" in obj and "/D" in obj.A:
        dest = obj.A.D
    if dest is None:
        return None
    # Named destination -> resolve
    if isinstance(dest, (pikepdf.String, pikepdf.Name)):
        dest = named_dests.get(str(dest))
        if dest is None:
            return None
    if isinstance(dest, pikepdf.Dictionary) and "/D" in dest:
        dest = dest.D
    if isinstance(dest, pikepdf.Array) and len(dest) > 0:
        page_obj = dest[0]
        try:
            return page_index.get(page_obj.objgen)
        except Exception:
            return None
    return None


# Flatten the outline into (depth, title, src_page_index).
flat = []
with src.open_outline() as outline:
    def walk(items, depth):
        for it in items:
            pidx = dest_to_page_index(it)
            flat.append((depth, str(it.title) if it.title else "", pidx))
            walk(it.children, depth + 1)
    walk(outline.root, 0)

print(f"Total pages: {total_pages} -> {total_chunks} files. Outline entries: {len(flat)}")

for chunk_idx in range(total_chunks):
    start = chunk_idx * PAGES_PER_CHUNK
    end = min(start + PAGES_PER_CHUNK, total_pages)

    dst = pikepdf.new()
    for page_num in range(start, end):
        dst.pages.append(src.pages[page_num])

    out_filename = os.path.join(
        OUTPUT_DIR, f"grc_part_{chunk_idx+1:03d}_pages_{start+1}-{end}.pdf"
    )

    # Rebuild bookmarks for entries landing in this chunk, remapped to local pages.
    kept = 0
    with dst.open_outline() as out:
        stack = []  # (depth, OutlineItem)
        for depth, title, pidx in flat:
            if pidx is None or not (start <= pidx < end):
                continue
            local = pidx - start
            node = pikepdf.OutlineItem(title)
            node.destination = pikepdf.Array([dst.pages[local].obj, pikepdf.Name.Fit])
            # find parent: nearest item on stack with smaller depth
            while stack and stack[-1][0] >= depth:
                stack.pop()
            if stack:
                stack[-1][1].children.append(node)
            else:
                out.root.append(node)
            stack.append((depth, node))
            kept += 1

    dst.remove_unreferenced_resources()
    dst.save(out_filename, compress_streams=True)
    dst.close()

    size_mb = os.path.getsize(out_filename) / (1024 * 1024)
    print(f"  ok {os.path.basename(out_filename)} ({size_mb:.1f} MB, {kept} bookmarks)")

src.close()
print(f"\nDone! {total_chunks} files saved to '{OUTPUT_DIR}/'")
