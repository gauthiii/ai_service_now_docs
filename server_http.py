"""Remote (Streamable HTTP) entrypoint for the ServiceNow AI docs MCP server.

This is ONLY for remote hosting (e.g. Render) so the server can be added to
claude.ai as a custom connector. It does not affect local usage: Claude Code
still launches `mcp_server.py` over stdio exactly as before.

It reuses the same tools/index/instructions from `mcp_server.py` by rebuilding a
FastMCP instance with the same registrations. Importing that module does NOT
start stdio, because its `mcp.run()` is guarded by `if __name__ == "__main__"`.

Auth: if OAUTH_ISSUER_URL / OAUTH_CLIENT_ID / OAUTH_CLIENT_SECRET are set (via
.env locally or Render env vars), the server is protected as an OAuth 2.0
Resource Server and verifies bearer tokens against the provider. If they are
NOT set, it runs unauthenticated (handy for a quick local HTTP smoke test).

Local test (no auth):
    PORT=8000 python server_http.py        # http://127.0.0.1:8000/mcp

On Render:
    Start command: python server_http.py
    Set OAUTH_* + MCP_PUBLIC_URL as environment variables in the dashboard.
    Connector URL: https://<name>.onrender.com/mcp
"""

import os

from dotenv import load_dotenv

load_dotenv()  # no-op if there's no .env (e.g. on Render, where you use env vars)

# Reuse the existing server (tools, index, instructions) unchanged.
from mcp_server import mcp

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))

ISSUER_URL = os.environ.get("OAUTH_ISSUER_URL")
CLIENT_ID = os.environ.get("OAUTH_CLIENT_ID")
CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET")
PUBLIC_URL = os.environ.get("MCP_PUBLIC_URL")  # this server's public https URL
REQUIRED_SCOPES = [s for s in os.environ.get("OAUTH_REQUIRED_SCOPES", "").split() if s]


def _configure_auth() -> None:
    """Attach OAuth Resource Server protection if the env is fully configured."""
    if not (ISSUER_URL and CLIENT_ID and CLIENT_SECRET and PUBLIC_URL):
        print("[server_http] OAuth env not set -> running UNAUTHENTICATED.")
        return

    from pydantic import AnyHttpUrl

    from mcp.server.auth.settings import AuthSettings
    from auth import IntrospectionTokenVerifier

    mcp._token_verifier = IntrospectionTokenVerifier(
        issuer_url=ISSUER_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        resource_url=PUBLIC_URL,
        required_scopes=REQUIRED_SCOPES,
    )
    mcp.settings.auth = AuthSettings(
        issuer_url=AnyHttpUrl(ISSUER_URL),
        resource_server_url=AnyHttpUrl(PUBLIC_URL),
        required_scopes=REQUIRED_SCOPES or None,
    )
    print(f"[server_http] OAuth enabled. Issuer={ISSUER_URL} Resource={PUBLIC_URL}")


def _configure_transport_security() -> None:
    """Allow the public host so the SDK's DNS-rebinding protection doesn't 421.

    When served behind a proxy (Render, ngrok), the incoming Host header is the
    public domain, which the SDK rejects by default. ALLOWED_HOSTS is a
    space/comma-separated list; defaults to "*" (any host) which is fine for a
    personal, read-only docs server.
    """
    from mcp.server.transport_security import TransportSecuritySettings

    raw = os.environ.get("ALLOWED_HOSTS", "*").strip()
    if raw == "*" or not raw:
        # Any host: turn protection off. The SDK treats "*" as a literal host,
        # not a wildcard, so we disable the check rather than allow-list "*".
        mcp.settings.transport_security = TransportSecuritySettings(
            enable_dns_rebinding_protection=False,
        )
        print("[server_http] DNS-rebinding protection OFF (ALLOWED_HOSTS=*)")
    else:
        hosts = [h for h in raw.replace(",", " ").split() if h]
        mcp.settings.transport_security = TransportSecuritySettings(
            enable_dns_rebinding_protection=True,
            allowed_hosts=hosts,
            allowed_origins=hosts,
        )
        print(f"[server_http] allowed_hosts={hosts}")


if __name__ == "__main__":
    _configure_auth()
    _configure_transport_security()
    mcp.settings.host = HOST
    mcp.settings.port = PORT
    mcp.run(transport="streamable-http")
