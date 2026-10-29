# Local developer API keys

Generate a unique credential with `python developer_keys.py`. Store the output privately; it is shown only once. The local `cryptoshield-keys.json` registry contains SHA-256 digests, not raw keys, and must never be committed.

Run `python api.py`. Health remains public on localhost. Scan and alerts require `Authorization: Bearer <key>`. Example:

```bash
curl -H "Authorization: Bearer YOUR_KEY" http://127.0.0.1:8787/v1/scan
```

Keys use Python's cryptographically secure `secrets` module. They are local development credentials, **not commercial entitlements**. There is no billing, expiry, rotation, quota enforcement, or remotely hosted authentication in this Community implementation. Protect the key registry and never expose the local API to the internet.
