"""Small dependency-free Python client for the local CryptoShield API."""
import json
from urllib.request import urlopen, Request

class CryptoShieldClient:
    def __init__(self, base_url="http://127.0.0.1:8787", api_key=None):
        if not (base_url.startswith("http://127.0.0.1:") or base_url.startswith("http://localhost:")):
            raise ValueError("Community API client only supports local loopback URLs")
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
    def _get(self, path):
        headers = {"Authorization": "Bearer " + self.api_key} if self.api_key else {}
        request = Request(self.base_url + path, headers=headers)
        with urlopen(request, timeout=15) as response:
            return json.load(response)
    def health(self):
        return self._get("/v1/health")
    def scan(self):
        return self._get("/v1/scan")
    def alerts(self):
        return self._get("/v1/alerts")
