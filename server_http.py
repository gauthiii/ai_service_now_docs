"""Remote (Streamable HTTP) entrypoint for the ServiceNow AI docs MCP server.

This is ONLY for remote hosting (e.g. Render) so the server can be added to
claude.ai as a custom connector. It does not affect local usage: Claude Code
still launches `mcp_server.py` over stdio exactly as before.

It reuses the same `mcp` instance (tools, index, instructions) from
`mcp_server.py`. Importing that module does NOT start stdio, because its
`mcp.run()` is guarded by `if __name__ == "__main__"`.

Local test:
    PORT=8000 python server_http.py
    # MCP endpoint: http://127.0.0.1:8000/mcp

On Render:
    Start command: python server_http.py
    Render injects $PORT and gives you https://<name>.onrender.com
    Connector URL: https://<name>.onrender.com/mcp
"""

import os

from mcp_server import mcp

if __name__ == "__main__":
    # Bind to all interfaces and the port the host provides (Render sets PORT).
    mcp.settings.host = os.environ.get("HOST", "0.0.0.0")
    mcp.settings.port = int(os.environ.get("PORT", "8000"))
    mcp.run(transport="streamable-http")
