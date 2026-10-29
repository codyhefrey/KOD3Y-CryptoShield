# CryptoShield Community API v1 (local prototype)

Run `python api.py`. Default address: `http://127.0.0.1:8787`.

| Method | Path | Result |
|---|---|---|
| GET | /v1/health | Service health and API version |
| GET | /v1/scan | Local process and Docker snapshot |
| GET | /v1/alerts | High-CPU investigation leads |
| POST | any | 405 (read-only) |

Example: `curl http://127.0.0.1:8787/v1/health`

Python SDK:
```python
from sdk.python.cryptoshield_client import CryptoShieldClient
client = CryptoShieldClient()
print(client.health())
print(client.alerts())
```

## Security boundaries
- The server binds only to 127.0.0.1. Do not reverse-proxy it or expose it on public interfaces.
- No CORS header is supplied. Do not treat localhost as a security boundary against all local processes.
- No authentication, quotas, TLS, multi-tenant isolation, remote collection, or containment exists in this edition.
- Process executable paths may be sensitive; avoid sharing raw scan responses.
- High CPU alone is not a malware verdict.
- API v1 is experimental; responses may change before a stable release.

## Developer keys (required for scan and alerts)

Run `python developer_keys.py` to create a unique local key, then pass `Authorization: Bearer YOUR_KEY` for `/v1/scan` and `/v1/alerts`. `/v1/health` requires no key. The Python client accepts `CryptoShieldClient(api_key="YOUR_KEY")`. See [credential guide](DEVELOPER_KEYS.md). This is not a hosted commercial authentication service.
