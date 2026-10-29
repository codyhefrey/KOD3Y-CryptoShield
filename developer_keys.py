"""Local developer credentials: random tokens, hashed on disk, no cloud billing."""
import argparse
import hashlib
import hmac
import json
import os
import secrets
from pathlib import Path

DEFAULT_STORE = "cryptoshield-keys.json"

def issue(path=DEFAULT_STORE):
    path = Path(path)
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = {"keys": {}}
    identifier = secrets.token_hex(8)
    token = "kcs_dev_" + identifier + "_" + secrets.token_urlsafe(32)
    data["keys"][identifier] = hashlib.sha256(token.encode()).hexdigest()
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return token

def verify(token, path=DEFAULT_STORE):
    if not isinstance(token, str) or len(token) > 256:
        return False
    parts = token.split("_", 3)
    if len(parts) != 4 or parts[:2] != ["kcs", "dev"]:
        return False
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    digest = data.get("keys", {}).get(parts[2])
    return isinstance(digest, str) and hmac.compare_digest(digest, hashlib.sha256(token.encode()).hexdigest())

def main():
    parser = argparse.ArgumentParser(description="Create a local CryptoShield developer key")
    parser.add_argument("--store", default=DEFAULT_STORE)
    args = parser.parse_args()
    token = issue(args.store)
    print("Save this key in a secret manager. It will not be shown again:")
    print(token)

if __name__ == "__main__":
    main()
