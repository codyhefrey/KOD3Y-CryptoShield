# KOD3Y CryptoShield — Community Edition

Defensive, read-only cryptojacking triage prototype by KOD3Y T3CH.

## Current capabilities
- Collect CPU usage from running processes (psutil).
- Inventory running Docker containers if Docker is installed.
- Export a local JSON report.
- Run unit tests and GitHub Actions checks.

**Limitations:** This is not an antivirus, continuous monitor, cryptominer signature scanner, or guarantee of protection. High CPU alone does not prove cryptojacking. No processes are stopped and no remote telemetry is sent.
## Setup for New Contributors

### Prerequisites

Before setting up the project, make sure you have:

- Python 3.10 or later
- Git
- A terminal or command prompt

### Clone the Repository

```bash
git clone https://github.com/codyhefrey/KOD3Y-CryptoShield.git
cd KOD3Y-CryptoShield
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate the environment on macOS or Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

After completing these steps, follow the Quick start instructions below to run the application and tests.

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
The Community edition includes an [Apache License 2.0](LICENSE). Contributions are welcome under the [contribution guidelines](CONTRIBUTING.md), subject to maintainer review. See [governance](docs/GOVERNANCE.md) and the [code of conduct](CODE_OF_CONDUCT.md). The proprietary Enterprise edition is maintained separately.

## Developer API (experimental)

Start `python api.py --port 8787` and query `http://127.0.0.1:8787/v1/health`.
See [API reference](docs/API.md) and [Python client](sdk/python/cryptoshield_client.py).
This API is local-only, read-only, unauthenticated, and not suitable for public exposure.
