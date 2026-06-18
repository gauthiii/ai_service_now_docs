"""OAuth token verification for the remote (HTTP) MCP server.

This is used ONLY by server_http.py for the Render deployment. The local stdio
server (mcp_server.py used by Claude Code) never imports this and is unaffected.

Model: this MCP server is an OAuth 2.0 *Resource Server*. An external provider
(Auth0 / Stytch / WorkOS AuthKit / Descope / ... ) is the Authorization Server.
claude.ai performs the login + Dynamic Client Registration against that provider,
obtains an access token, and sends it as `Authorization: Bearer <token>`.

We verify each token by calling the provider's RFC 7662 introspection endpoint,
authenticating that call with OAUTH_CLIENT_ID / OAUTH_CLIENT_SECRET. The
introspection endpoint is discovered from the provider's OIDC/OAuth metadata.
"""

from __future__ import annotations

import time
from typing import Optional

import httpx

from mcp.server.auth.provider import AccessToken, TokenVerifier


class IntrospectionTokenVerifier(TokenVerifier):
    """Verifies bearer tokens via the provider's token introspection endpoint."""

    def __init__(
        self,
        issuer_url: str,
        client_id: str,
        client_secret: str,
        resource_url: str,
        required_scopes: Optional[list[str]] = None,
    ) -> None:
        self.issuer_url = issuer_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.resource_url = resource_url.rstrip("/")
        self.required_scopes = required_scopes or []
        self._introspection_endpoint: Optional[str] = None

    async def _discover_introspection_endpoint(self) -> str:
        """Find the introspection endpoint from OIDC/OAuth discovery metadata."""
        if self._introspection_endpoint:
            return self._introspection_endpoint

        # Try OAuth Authorization Server metadata, then OIDC config.
        candidates = [
            f"{self.issuer_url}/.well-known/oauth-authorization-server",
            f"{self.issuer_url}/.well-known/openid-configuration",
        ]
        async with httpx.AsyncClient(timeout=10.0) as client:
            for url in candidates:
                try:
                    resp = await client.get(url)
                    if resp.status_code == 200:
                        endpoint = resp.json().get("introspection_endpoint")
                        if endpoint:
                            self._introspection_endpoint = endpoint
                            return endpoint
                except httpx.HTTPError:
                    continue
        raise RuntimeError(
            "Could not discover an introspection_endpoint from the OAuth provider "
            f"at {self.issuer_url}. Confirm OAUTH_ISSUER_URL is correct and that the "
            "provider exposes RFC 7662 token introspection."
        )

    async def verify_token(self, token: str) -> AccessToken | None:
        try:
            endpoint = await self._discover_introspection_endpoint()
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(
                    endpoint,
                    data={"token": token, "token_type_hint": "access_token"},
                    auth=(self.client_id, self.client_secret),
                    headers={"Accept": "application/json"},
                )
        except (httpx.HTTPError, RuntimeError):
            return None

        if resp.status_code != 200:
            return None

        data = resp.json()
        if not data.get("active", False):
            return None

        # Scope may come back as a space-delimited string per RFC 7662.
        raw_scope = data.get("scope", "")
        scopes = raw_scope.split() if isinstance(raw_scope, str) else list(raw_scope)

        # Enforce that the token carries every required scope, if any.
        if self.required_scopes and not set(self.required_scopes).issubset(scopes):
            return None

        return AccessToken(
            token=token,
            client_id=data.get("client_id", ""),
            scopes=scopes,
            expires_at=int(data["exp"]) if data.get("exp") else None,
            resource=self.resource_url,
            subject=data.get("sub"),
            claims=data,
        )
