"""CryptoShield v1 local-only, read-only HTTP API. No remote binding or CORS."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
from cryptoshield import collect

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/v1/health":
            self.respond(200, {"status": "ok", "service": "cryptoshield", "version": "v1"})
        elif path == "/v1/scan":
            self.respond(200, collect())
        elif path == "/v1/alerts":
            from monitor import assess
            snapshot = collect(80)
            self.respond(200, {"alerts": assess(snapshot, 80), "note": "Investigation leads, not malware verdicts"})
        else:
            self.respond(404, {"error": "not_found"})
    def do_POST(self):
        self.respond(405, {"error": "read_only_api"})
    def respond(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("port must be between 1024 and 65535")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"CryptoShield local API: http://127.0.0.1:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
