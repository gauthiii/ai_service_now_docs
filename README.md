# ServiceNow AI Practices Documentation — MCP Server

An MCP (Model Context Protocol) server that exposes the official ServiceNow AI
documentation as searchable, LLM-readable context. It covers three practice areas
on the latest ServiceNow releases (**Zurich** and **Australia**):

- **ServiceNow Enable AI** — AI Implementation (Now Assist, AI Agents, Now Assist
  Skill Kit, AI Control Tower, Predictive Intelligence, Document Intelligence,
  Natural Language Understanding/Query, MCP Server Console, Knowledge Graph, …)
- **ServiceNow GRC** — Governance, Risk, and Compliance (AI Risk and Compliance:
  governance life cycle, risk/impact assessments, AI use cases, issues, controls,
  and frameworks such as NIST RMF and the EU AI Act)
- **AI Control Tower Implementation** — the detailed AICT implementation guide
  (lifecycle phases: General, Discover, Govern, Assess, Build & Test, Deploy,
  Observe, Measure; plus cross-product integrations: AI Strategy/SPM, AI Gateway,
  AI Case Management, CMDB)

The documentation is organized as **main document → topic → subtopic**, where each
subtopic is a single markdown file (~1,600 subtopics total). The exact count is
computed live by the server at startup, so it is always accurate.

---

## Table of contents

1. [Pipeline overview](#pipeline-overview)
2. [Prerequisites](#prerequisites)
3. [Step 1 — Create PDF chunks](#step-1--create-pdf-chunks)
4. [Step 2 — Produce the markdown docs](#step-2--produce-the-markdown-docs)
5. [Step 3 — Run / build the MCP server](#step-3--run--build-the-mcp-server)
6. [Step 4 — Register the MCP server](#step-4--register-the-mcp-server)
7. [Step 5 — Use it](#step-5--use-it)
8. [Remote hosting (claude.ai custom connector)](#remote-hosting-claudeai-custom-connector)
9. [Tools reference](#tools-reference)
10. [Project layout](#project-layout)
11. [License](#license)

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
`.md` file per subtopic** — under the main-document folders:

```
ServiceNow Enable AI/<Topic>/<Subtopic>.md
ServiceNow GRC/<Topic>/<Subtopic>.md
AI Control Tower Implementation/<Topic>/<Subtopic>.md
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

## How the MCP server works (internals)

Everything below happens **once, at process startup**, in
[`mcp_server.py`](mcp_server.py). The corpus is static while the server runs, so
nothing is re-read from disk per request.

### 1. Indexing — `build_index()`

Walks each folder in `MAIN_DOCUMENTS` and treats the tree as
**main document → topic → subtopic**:

- Only `MAIN_DOCUMENTS/<Topic>/<file>.md` (exactly two levels deep) is indexed.
  Loose `.md` at a document root, and anything under `_assets/` or deeper, is
  **ignored** — `validate_structure.py` (below) guards against accidental
  orphans.
- **Topic name** comes from the folder, with the leading order prefix stripped
  (`"19 - Document Intelligence"` → `"Document Intelligence"`) via `_TOPIC_PREFIX`.
- **Subtopic name + description** are parsed by `_extract_name_and_description()`,
  which handles both file shapes: those with a `## SOURCE INFORMATION` block
  (prefers `SUBSECTION NAME:`) and plain `# Title` + body files (first
  substantial paragraph becomes the description).
- **`subtopic_id`** is a deterministic slug: `slug(doc)__slug(topic)__slug(name)`,
  with a short md5 suffix appended only on collision. IDs are stable across
  restarts as long as the names don't change.
- Each file's lower-cased body is cached in `Subtopic.body_lc` so search never
  touches the disk again.

The result is `INDEX: dict[subtopic_id -> Subtopic]`.

### 2. Search ranking — `build_search_index()` + `bm25_search()`

`search_documentation` is a proper ranked search, not substring counting:

- An in-memory **inverted index** (`SEARCH`) maps each term → the subtopics
  containing it, with per-document term frequencies and lengths.
- **Light stemming** (`_stem`) normalizes a few common suffixes
  (`controls`/`control`, `assessing`/`assess`) so paraphrased queries still hit.
  The same stemmer runs on both indexed text and the query, so they always agree.
- **Field boosting**: tokens from the subtopic **name** (×5) and **topic** (×2)
  count more than body tokens, so a title match outranks an incidental body
  mention.
- **BM25 scoring** (`k1=1.5`, `b=0.75`) weights rare query terms higher (idf) and
  normalizes for document length, so long files don't win just by being long.
  Each result carries a `relevance` score.

It is pure standard-library Python — no external search engine or embeddings.

### 3. Server surface

- Server name advertised to clients: **`ServiceNow AI Practices Documentation`**.
- **Server instructions** (auto-sent on connect) and the **`how_to_use` prompt**
  both report the **live** subtopic count from `len(INDEX)` — it can never go
  stale.
- `mcp.run()` is guarded by `if __name__ == "__main__"`, so importing the module
  (for tests / the HTTP wrapper) never starts the stdio loop.

### 4. Structure validation — `validate_structure.py`

A dependency-free guard that fails (non-zero exit) on coverage-affecting
problems — orphaned root `.md` files, missing main folders — and warns on
cosmetic ones (empty topic folders, deep non-`_assets` files):

```bash
python validate_structure.py
```

It runs automatically via:

- **CI** — [`.github/workflows/validate-docs.yml`](.github/workflows/validate-docs.yml)
  on every push/PR that touches the docs or server.
- **Pre-commit hook** (optional, local) — install once:

  ```bash
  ln -sf ../../scripts/pre-commit .git/hooks/pre-commit
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
| `list_documents()`                                | List the main documents with topic/subtopic counts. **Start here.**           |
| `list_topics(document)`                           | List the topics within a main document.                                       |
| `list_subtopics(document, topic)`                 | List a topic's subtopics, each with its `subtopic_id` and short description.  |
| `search_documentation(query, document?, limit?)`  | BM25-ranked search across all subtopics (field-boosted, light stemming); returns ranked matches with ids + relevance. |
| `get_subtopic(subtopic_id)`                       | Return the **full markdown content + metadata** for one subtopic.             |

**Recommended order**

- Specific question / unknown location → `search_documentation()` → `get_subtopic()`.
- Browsing / "what's covered" → `list_documents()` → `list_topics()` →
  `list_subtopics()` → `get_subtopic()`.

Also available: the **`how_to_use`** MCP prompt, which returns the full usage
guide plus a live index count.

---

## Remote hosting (claude.ai custom connector)

Everything above runs the server **locally over stdio** for Claude Code / Claude
Desktop. To use the same docs server from the **claude.ai browser chat**, it has
to run as a remote service over **Streamable HTTP** at a public HTTPS URL, then be
added as a *custom connector*.

> **This is fully additive.** The remote setup lives in separate files
> ([`server_http.py`](server_http.py), [`auth.py`](auth.py)) and never touches the
> local stdio path — `mcp_server.py` is reused unchanged. Importing it does not
> start stdio (its `mcp.run()` is guarded by `if __name__ == "__main__"`).

### Files involved

| File                | Role                                                                 |
| ------------------- | -------------------------------------------------------------------- |
| `server_http.py`    | HTTP entrypoint — reuses the `mcp` instance and serves Streamable HTTP |
| `auth.py`           | Optional OAuth 2.0 token verification (used only when configured)     |
| `.env.example`      | Template for the remote/OAuth environment variables                  |
| `.env`              | Local secrets — **git-ignored**, never committed                     |
| `requirements.txt`  | Runtime deps for the host (`mcp`, `python-dotenv`, `httpx`)           |

### Environment variables

All are read by `server_http.py` only. Locally they come from `.env`; on a host
like Render, set them in the dashboard instead of committing `.env`.

| Variable               | Required? | Purpose                                                            |
| ---------------------- | --------- | ------------------------------------------------------------------ |
| `PORT`                 | auto      | Listen port. Render injects this automatically (defaults to 8000). |
| `HOST`                 | no        | Bind address (defaults to `0.0.0.0`).                              |
| `ALLOWED_HOSTS`        | no        | Space/comma list of allowed `Host` headers. Defaults to `*`, which **disables DNS-rebinding protection** — required behind a proxy (see note below). |
| `MCP_PUBLIC_URL`       | OAuth     | This server's own public HTTPS URL (its resource identifier).      |
| `OAUTH_ISSUER_URL`     | OAuth     | Your OAuth provider (Authorization Server) base URL.               |
| `OAUTH_CLIENT_ID`      | OAuth     | Client ID used to call the provider's token-introspection endpoint. |
| `OAUTH_CLIENT_SECRET`  | OAuth     | Client secret for that introspection call.                         |
| `OAUTH_REQUIRED_SCOPES`| no        | Space-separated scopes a token must carry to be accepted.          |

If the four OAuth variables are **unset**, the server runs **unauthenticated** —
fine for personal use of read-only public docs.

> **⚠️ The `Host`-header / 421 gotcha.** The MCP SDK enables DNS-rebinding
> protection by default and **rejects any request whose `Host` header isn't
> localhost with HTTP 421** (`Invalid Host header`). Behind a proxy (Render,
> ngrok) the incoming Host is the public domain, so this fires. When it does,
> claude.ai can't complete the handshake and falls back to an OAuth attempt,
> surfacing a misleading *"Couldn't register with the sign-in service"* error.
> The default `ALLOWED_HOSTS=*` disables the check and resolves it. Note `*` is a
> literal in the SDK (not a wildcard), so the code disables protection entirely
> rather than allow-listing `*`; set an explicit host list to keep it on.

### Local HTTP test

```bash
.venv/bin/pip install -r requirements.txt
PORT=8000 .venv/bin/python server_http.py     # endpoint: http://127.0.0.1:8000/mcp
```

A plain `GET /mcp` returns `406` (it needs MCP headers) — that's healthy. To
simulate a proxied request:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST http://127.0.0.1:8000/mcp \
  -H "Host: anything.example.com" \
  -H "Accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"t","version":"1"}}}'
# expect 200 (would be 421 if the Host check were on)
```

### Deploy to Render

1. Push the repo to GitHub. The big files (`*.pdf`, `*_chunks/`) and secrets
   (`.env`) are git-ignored, so only the code and the ~6 MB of `.md` docs ship.
2. Create a **Web Service** pointed at the repo:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python server_http.py`
3. (Optional) Set `OAUTH_*` + `MCP_PUBLIC_URL` env vars to enable auth. Leave
   them unset for an open, personal server.
4. Render gives you `https://<name>.onrender.com`. The connector URL is that plus
   `/mcp`.

> Render's free tier spins the service down when idle, so the first request after
> a nap cold-starts (~30–60 s) and claude.ai may time out once — just retry.

### Add it in claude.ai

**Settings → Connectors → Add custom connector** → paste
`https://<name>.onrender.com/mcp`. (Custom connectors require a paid claude.ai
plan.) With auth off it connects immediately; with auth on, claude.ai runs the
OAuth login against your provider.

### Optional: enabling OAuth

The server acts as an OAuth 2.0 **Resource Server**. An external provider is the
Authorization Server; claude.ai logs in there (via Dynamic Client Registration)
and sends a bearer token, which `auth.py` validates against the provider's
RFC 7662 introspection endpoint using `OAUTH_CLIENT_ID` / `OAUTH_CLIENT_SECRET`.

- The provider **must support Dynamic Client Registration**. Free tiers that do:
  **WorkOS AuthKit**, **Stytch**, **Descope** (and **Auth0** with DCR enabled).
- Create an application in the provider, then set `OAUTH_ISSUER_URL`,
  `OAUTH_CLIENT_ID`, `OAUTH_CLIENT_SECRET`, and `MCP_PUBLIC_URL` (the exact Render
  URL) and redeploy.
- Hardcoding fake OAuth values does **not** work — claude.ai performs a real
  handshake against the issuer and will fail if it isn't a live provider.

---

## Using it with Claude, ChatGPT, and Gemini

The server is available two ways. Pick whichever your client supports:

| Transport | Address | Best for |
| --------- | ------- | -------- |
| **Remote (Streamable HTTP)** | `https://ai-service-now-docs.onrender.com/mcp` | Browser/desktop apps and hosted agents — nothing to install |
| **Local (stdio)** | `python mcp_server.py` (after cloning) | CLIs and offline use |

> **Auth:** the hosted endpoint is currently **open / unauthenticated** (it serves
> read-only public documentation). OAuth can be turned on later via the `OAUTH_*`
> environment variables — see [Optional: enabling OAuth](#optional-enabling-oauth).
> If/when that happens, the clients below will prompt for sign-in automatically.

> **Cold start:** the host is on Render's free tier and sleeps when idle, so the
> first request after a pause can take ~30–60 s. If a client times out once on
> connect, just retry.

### Claude

- **Claude Code (CLI), remote:**
  ```bash
  claude mcp add --transport http servicenow-ai-docs https://ai-service-now-docs.onrender.com/mcp
  ```
  Or **local stdio** (after cloning this repo) — see
  [Step 4 — Register the MCP server](#step-4--register-the-mcp-server).
- **Claude Desktop / claude.ai (browser):**
  **Settings → Connectors → Add custom connector**, paste
  `https://ai-service-now-docs.onrender.com/mcp`. (Custom connectors require a
  paid plan.) See [Add it in claude.ai](#add-it-in-claudeai).

### ChatGPT

**A. Developer Mode connector (no code).** In ChatGPT,
**Settings → Connectors → Advanced → Developer mode**, then **Create / Add**
a connector with:
- **MCP Server URL:** `https://ai-service-now-docs.onrender.com/mcp`
- **Authentication:** None (the endpoint is open)

The five tools then appear in the composer's tool list. Developer Mode (full MCP
tool access) requires a paid ChatGPT plan and may be rolled out gradually.

**B. OpenAI API / Agents SDK (for apps).** Pass it as a hosted/remote MCP tool so
the model can call it server-side:

```python
from openai import OpenAI
client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[{
        "type": "mcp",
        "server_label": "servicenow_ai_docs",
        "server_url": "https://ai-service-now-docs.onrender.com/mcp",
        "require_approval": "never",   # endpoint is read-only + unauthenticated
    }],
    input="How do I configure Document Intelligence in ServiceNow?",
)
print(resp.output_text)
```

(With the Agents SDK, use its `HostedMCPTool` / remote-MCP equivalent pointing at
the same `server_url`.)

### Gemini

**A. Gemini CLI (no code).** Add the server to `~/.gemini/settings.json`:

```jsonc
{
  "mcpServers": {
    "servicenow-ai-docs": {
      "httpUrl": "https://ai-service-now-docs.onrender.com/mcp"
    }
  }
}
```

For **local stdio** instead, use `"command"` + `"args"` (absolute paths):

```jsonc
{
  "mcpServers": {
    "servicenow-ai-docs": {
      "command": "/ABSOLUTE/PATH/.venv/bin/python",
      "args": ["/ABSOLUTE/PATH/mcp_server.py"]
    }
  }
}
```

Run `gemini`, then `/mcp` to confirm the tools are listed.

**B. Gemini API / `google-genai` SDK (for apps).** The SDK can call an MCP
session directly with automatic function calling:

```python
import asyncio
from google import genai
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://ai-service-now-docs.onrender.com/mcp"

async def main():
    client = genai.Client()
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            resp = await client.aio.models.generate_content(
                model="gemini-2.5-flash",
                contents="What is the AI governance life cycle in ServiceNow GRC?",
                config=genai.types.GenerateContentConfig(tools=[session]),
            )
            print(resp.text)

asyncio.run(main())
```

> **Note:** Gemini has no built-in "remote connector" inside the consumer Gemini
> app the way ChatGPT/Claude do — MCP is consumed through the **Gemini CLI** or
> the **API/SDK** as shown above.

---

## FAQ

**1. How is this context collected, and how up to date is it?**
The content is extracted from ServiceNow's official product documentation PDFs
for the **Zurich** and **Australia** releases — the three practice areas *ServiceNow
Enable AI* (AI implementation), *ServiceNow GRC* (governance, risk, and
compliance), and *AI Control Tower Implementation* (the detailed AICT
implementation guide). The pipeline is: source PDF → page-bounded PDF chunks
([`split_pikepdf.py`](split_pikepdf.py)) → one markdown file per subtopic under
the document folders. It is a **point-in-time snapshot**, not a live mirror of
docs.servicenow.com — it only updates when the `.md` files in this repo are
regenerated and committed. The corpus currently holds ~1,600 subtopics; the server
reports the exact live count via `list_documents()` and the `how_to_use` prompt.

**2. How is the indexing done?**
At **startup**, `build_index()` walks `MAIN_DOCUMENTS/<Topic>/<file>.md` (exactly
two levels deep) and builds an in-memory index keyed by a stable `subtopic_id`
(`slug(doc)__slug(topic)__slug(name)`). For each file it derives a display name and
short description, and caches the lower-cased body. It then builds a **BM25
inverted index** (`build_search_index()`): tokenized + lightly stemmed terms with
field boosting (name ×5, topic ×2, description ×2, body ×1). Everything is in
memory and pure standard-library — no database, no embeddings, no per-query disk
reads. See [How the MCP server works (internals)](#how-the-mcp-server-works-internals).

**3. How will the LLM know which topic to search for?**
On connect, the server sends **instructions** (and exposes the `how_to_use`
prompt) describing the main documents, the topic list, and the recommended tool
order. From there the model typically calls `search_documentation(query)` —
which is BM25-ranked, so the most relevant subtopics surface first regardless of
which topic they live in — then `get_subtopic(id)` to read full content. For
browsing, it can drill `list_documents()` → `list_topics()` → `list_subtopics()`.
The model never has to guess the topic up front; search spans the whole corpus.

**4. How do I make this MCP server work *and* keep the LLM's own search/tools active?**
MCP tools are **additive** — adding this connector does not disable the model's
built-in web search, code interpreter, or other tools. They coexist, and the model
chooses per query. To bias it toward grounded answers, instruct it explicitly,
e.g. *"For anything about ServiceNow AI or GRC, use the `servicenow-ai-docs` tools
and cite document → topic → subtopic; use web search only for things outside that
documentation."* The server's own instructions already tell the model to prefer
this source for ServiceNow AI/GRC topics. In API/SDK setups you can list this MCP
server alongside web-search/other tools in the same `tools` array.

**5. Which tools does the server expose, and in what order should they be used?**
Five: `list_documents`, `list_topics`, `list_subtopics`, `search_documentation`,
`get_subtopic`, plus the `how_to_use` prompt. Recommended order:
`search_documentation` → `get_subtopic` for a specific question;
`list_documents` → `list_topics` → `list_subtopics` → `get_subtopic` for browsing.
See the [Tools reference](#tools-reference).

**6. Is any of my data or queries stored or sent to ServiceNow?**
No. The server is **read-only** and self-contained — it only reads the bundled
`.md` files and returns matches. It makes no outbound calls to ServiceNow or any
third party, and it does not persist queries. (The only optional network
dependency is OAuth token introspection, and only if you enable auth.)

**7. Why might the first request be slow or fail once?**
The hosted endpoint runs on Render's free tier, which **sleeps when idle**. The
first request after a nap cold-starts the service (~30–60 s) and a client may time
out once — retry and it connects. The local stdio server has no such delay.

**8. How do I add new documentation or fix a missing topic?**
Add `.md` files under `MAIN_DOCUMENTS/<Topic>/` (exactly that depth — loose files
at a document root or under `_assets/` are **not** indexed). Run
`python validate_structure.py` to confirm nothing is orphaned, restart the server
(the index rebuilds at startup), and redeploy if using the hosted endpoint. CI
([`.github/workflows/validate-docs.yml`](.github/workflows/validate-docs.yml)) and
the optional pre-commit hook enforce the structure automatically.

---

## Project layout

```
.
├── split_pikepdf.py            # PDF → page-bounded PDF chunks (bookmarks preserved)
├── mcp_server.py               # the MCP server (index + BM25 search + tools + instructions + prompt)
├── validate_structure.py       # guard: flags docs the server can't index (CI + pre-commit)
├── scripts/pre-commit          # optional local git hook → runs validate_structure.py
├── .github/workflows/validate-docs.yml  # CI: validate structure + build index on push/PR
├── server_http.py              # remote entrypoint: Streamable HTTP for claude.ai
├── auth.py                     # optional OAuth token verification (HTTP server only)
├── requirements.txt            # runtime deps for remote hosting
├── .env.example                # template for remote/OAuth env vars
├── ServiceNow Enable AI/       # main document: AI Implementation
│   └── <Topic>/<Subtopic>.md
├── ServiceNow GRC/             # main document: Governance, Risk, and Compliance
│   └── <Topic>/<Subtopic>.md
├── AI Control Tower Implementation/  # main document: AICT implementation guide
│   └── <Topic>/<Subtopic>.md
├── grc_chunks/                 # generated PDF chunks (GRC)
├── enable_ai_chunks/           # generated PDF chunks (Enable AI)
├── aict_implementation_chunks/ # generated PDF chunks (AI Control Tower)
├── README.md
└── LICENSE
```

> Note: `*.pdf`, `.venv/`, `__pycache__/`, `.env`, `grc_chunks/`,
> `enable_ai_chunks/`, and `aict_implementation_chunks/` are git-ignored.
>
> The source PDFs (`servicenow_*.pdf`) and the generated chunk PDFs
> (`grc_chunks/`, `enable_ai_chunks/`) are **intentionally not committed** — they
> are large binary files kept **only on the author's local machine**. They are
> not part of the repository. Regenerate the chunks from your own source PDFs by
> following [Step 1 — Create PDF chunks](#step-1--create-pdf-chunks).

---

## License

[MIT](LICENSE) © 2026 Gautham Vijayaraj
