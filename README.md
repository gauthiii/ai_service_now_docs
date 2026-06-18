# ServiceNow AI Practices Documentation — MCP Server

An MCP (Model Context Protocol) server that exposes the official ServiceNow AI
documentation as searchable, LLM-readable context. It covers two practice areas
on the latest ServiceNow releases (**Zurich** and **Australia**):

- **ServiceNow Enable AI** — AI Implementation (Now Assist, AI Agents, Now Assist
  Skill Kit, AI Control Tower, Predictive Intelligence, Document Intelligence,
  Natural Language Understanding/Query, MCP Server Console, Knowledge Graph, …)
- **ServiceNow GRC** — Governance, Risk, and Compliance (AI Risk and Compliance:
  governance life cycle, risk/impact assessments, AI use cases, issues, controls,
  and frameworks such as NIST RMF and the EU AI Act)

The documentation is organized as **main document → topic → subtopic**, where each
subtopic is a single markdown file (~319 subtopics total).

---

## Table of contents

1. [Pipeline overview](#pipeline-overview)
2. [Prerequisites](#prerequisites)
3. [Step 1 — Create PDF chunks](#step-1--create-pdf-chunks)
4. [Step 2 — Produce the markdown docs](#step-2--produce-the-markdown-docs)
5. [Step 3 — Run / build the MCP server](#step-3--run--build-the-mcp-server)
6. [Step 4 — Register the MCP server](#step-4--register-the-mcp-server)
7. [Step 5 — Use it](#step-5--use-it)
8. [Tools reference](#tools-reference)
9. [Project layout](#project-layout)
10. [License](#license)

---

## Pipeline overview

```
servicenow_*.pdf  ──split_pikepdf.py──▶  *_chunks/*.pdf
       (large source PDFs)                 (100/50-page PDF chunks, bookmarks preserved)

*_chunks/*.pdf  ──(content extraction)──▶  ServiceNow <Doc>/<Topic>/<Subtopic>.md
                                            (one md file per subtopic)

ServiceNow <Doc>/.../*.md  ──mcp_server.py──▶  MCP server: "ServiceNow AI Practices Documentation"
                                                (index + search + fetch tools)
```

---

## Prerequisites

- Python 3.10+
- A virtual environment with the dependencies installed:

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install pikepdf "mcp[cli]"
```

> All commands below assume you run from the project root and use the venv's
> Python (`.venv/bin/python`).

---

## Step 1 — Create PDF chunks

Large source PDFs are split into smaller, page-bounded chunks while preserving
bookmarks/outlines, using [`split_pikepdf.py`](split_pikepdf.py).

1. Place the source PDF in the project root (e.g. `servicenow_grc.pdf`).
2. Edit the configuration constants at the top of `split_pikepdf.py`:

   ```python
   INPUT_PDF       = os.path.join(BASE, "servicenow_grc.pdf")  # source PDF
   PAGES_PER_CHUNK = 100                                        # pages per chunk
   OUTPUT_DIR      = os.path.join(BASE, "grc_chunks")           # output folder
   ```

3. Run it:

   ```bash
   .venv/bin/python split_pikepdf.py
   ```

Output: a folder of `*_part_NNN_pages_X-Y.pdf` files, each with bookmarks remapped
to local page numbers. Repeat for each source PDF (adjust the three constants).

---

## Step 2 — Produce the markdown docs

From the PDF chunks, the documentation content is extracted into markdown — **one
`.md` file per subtopic** — under the two main-document folders:

```
ServiceNow Enable AI/<Topic>/<Subtopic>.md
ServiceNow GRC/<Topic>/<Subtopic>.md
```

Each md file is the content of a single subtopic. Two markdown shapes are
supported by the server:

- Files with a `## SOURCE INFORMATION` block (with `SECTION NAME` / `SUBSECTION
  NAME` metadata), and
- Plain files that start with a `# Title` followed by body text.

> The server reads whatever `.md` files exist under those folders, so this step
> can be done by any extraction process as long as the folder structure
> (`main document → topic → subtopic.md`) is followed. Files inside `_assets/`
> sub-folders are ignored.

---

## Step 3 — Run / build the MCP server

The server is [`mcp_server.py`](mcp_server.py). It indexes all subtopics at
startup and serves them over **stdio**.

- The top-level folders it indexes are configured in `MAIN_DOCUMENTS` inside
  `mcp_server.py`.
- The server name advertised to clients is **`ServiceNow AI Practices
  Documentation`**.
- It ships with **server instructions** (auto-sent to the LLM on connect) and a
  **`how_to_use` prompt** explaining what the server is and the order to use the
  tools.

Run it directly (it will wait for an MCP client on stdio):

```bash
.venv/bin/python mcp_server.py
```

Quick self-check that it loads and indexes correctly:

```bash
.venv/bin/python -c "import mcp_server as m; print('subtopics:', len(m.INDEX))"
```

---

## Step 4 — Register the MCP server

Two rules that matter most: use the **venv's Python** as the command, and use
**absolute paths** for everything (MCP servers don't inherit your shell's working
directory).

### Claude Code (CLI)

```bash
# from the project root
claude mcp add servicenow-ai-docs -- \
  "$PWD/.venv/bin/python" "$PWD/mcp_server.py"
```

Choose a scope with `-s`:

| Scope            | Flag         | Stored in                         | Use when                    |
| ---------------- | ------------ | --------------------------------- | --------------------------- |
| Local (default)  | `-s local`   | `~/.claude.json` (this project)   | personal, single project    |
| Project (shared) | `-s project` | `.mcp.json` in the repo (commit)  | share with teammates        |
| User (global)    | `-s user`    | user config (all projects)        | available everywhere        |

Manage it:

```bash
claude mcp list                      # list servers + health (look for ✓ Connected)
claude mcp get servicenow-ai-docs    # show this server's config
claude mcp remove servicenow-ai-docs # unregister
```

After adding, restart Claude Code or run `/mcp` to activate it.

### Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "servicenow-ai-docs": {
      "command": "/ABSOLUTE/PATH/.venv/bin/python",
      "args": ["/ABSOLUTE/PATH/mcp_server.py"]
    }
  }
}
```

Then fully quit and reopen Claude Desktop.

---

## Step 5 — Use it

Once registered and connected, the LLM automatically receives the server
instructions describing what the documentation covers and how to navigate it.
Ask natural questions, for example:

- "How do I configure Document Intelligence in ServiceNow?"
- "What is the AI governance life cycle in ServiceNow GRC?"
- "How do I run a risk assessment on an AI asset?"

The model resolves these by calling the tools (typically
`search_documentation` → `get_subtopic`). In Claude Code, the tools appear as
`mcp__servicenow-ai-docs__<tool_name>`, and the prompt as `how_to_use`.

---

## Tools reference

| Tool                                              | Purpose                                                                       |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| `list_documents()`                                | List the two main documents with topic/subtopic counts. **Start here.**       |
| `list_topics(document)`                           | List the topics within a main document.                                       |
| `list_subtopics(document, topic)`                 | List a topic's subtopics, each with its `subtopic_id` and short description.  |
| `search_documentation(query, document?, limit?)`  | Full-text search across all subtopics; returns ranked matches with ids.       |
| `get_subtopic(subtopic_id)`                       | Return the **full markdown content + metadata** for one subtopic.             |

**Recommended order**

- Specific question / unknown location → `search_documentation()` → `get_subtopic()`.
- Browsing / "what's covered" → `list_documents()` → `list_topics()` →
  `list_subtopics()` → `get_subtopic()`.

Also available: the **`how_to_use`** MCP prompt, which returns the full usage
guide plus a live index count.

---

## Project layout

```
.
├── split_pikepdf.py            # PDF → page-bounded PDF chunks (bookmarks preserved)
├── mcp_server.py               # the MCP server (index + tools + instructions + prompt)
├── ServiceNow Enable AI/       # main document: AI Implementation
│   └── <Topic>/<Subtopic>.md
├── ServiceNow GRC/             # main document: Governance, Risk, and Compliance
│   └── <Topic>/<Subtopic>.md
├── grc_chunks/                 # generated PDF chunks (GRC)
├── enable_ai_chunks/           # generated PDF chunks (Enable AI)
├── README.md
└── LICENSE
```

> Note: `*.pdf`, `.venv/`, and `__pycache__/` are git-ignored.
>
> The source PDFs (`servicenow_*.pdf`) and the generated chunk PDFs
> (`grc_chunks/`, `enable_ai_chunks/`) are **intentionally not committed** — they
> are large binary files kept **only on the author's local machine**. They are
> not part of the repository. Regenerate the chunks from your own source PDFs by
> following [Step 1 — Create PDF chunks](#step-1--create-pdf-chunks).

---

## License

[MIT](LICENSE) © 2026 Gautham Vijayaraj
