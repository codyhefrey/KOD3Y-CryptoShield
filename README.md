# KOD3Y CryptoShield — Community Edition

Defensive, read-only cryptojacking triage prototype by KOD3Y T3CH.

## Current capabilities
- Collect CPU usage from running processes (psutil).
- Inventory running Docker containers if Docker is installed.
- Export a local JSON report.
- Run unit tests and GitHub Actions checks.

**Limitations:** This is not an antivirus, continuous monitor, cryptominer signature scanner, or guarantee of protection. High CPU alone does not prove cryptojacking. No processes are stopped and no remote telemetry is sent.

## Quick start
Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python cryptoshield.py --cpu-threshold 50 --output cryptoshield-report.json
python -m unittest discover -s tests -v
```

Run only on devices you own or are authorized to assess. Reports may include local executable paths; keep them private.

## Development
See [roadmap](docs/ROADMAP.md) and [security policy](SECURITY.md).

## Licensing
A public license has not yet been selected; public visibility alone does not grant redistribution rights. Do not assume the code is open-source licensed until a license is added.

## Developer API (experimental)

Start `python api.py --port 8787` and query `http://127.0.0.1:8787/v1/health`.
See [API reference](docs/API.md) and [Python client](sdk/python/cryptoshield_client.py).
This API is local-only, read-only, unauthenticated, and not suitable for public exposure.
