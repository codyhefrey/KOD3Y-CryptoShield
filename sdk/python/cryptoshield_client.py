"""Small dependency-free Python client for the local CryptoShield API."""
import json
from urllib.request import urlopen

class CryptoShieldClient:
    def __init__(self, base_url="http://127.0.0.1:8787"):
        if not (base_url.startswith("http://127.0.0.1:") or base_url.startswith("http://localhost:")):
            raise ValueError("Community API client only supports local loopback URLs")
        self.base_url = base_url.rstrip("/")
    def _get(self, path):
        with urlopen(self.base_url + path, timeout=15) as response:
            return json.load(response)
    def health(self):
        return self._get("/v1/health")
    def scan(self):
        return self._get("/v1/scan")
    def alerts(self):
        return self._get("/v1/alerts")
