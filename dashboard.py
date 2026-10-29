"""Minimal local dashboard using only the Python standard library.
Bind to loopback only; never expose this server to the internet.
"""
import argparse
import html
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(BaseHTTPRequestHandler):
    report_path = "cryptoshield-monitor.jsonl"
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        entries = []
        path = Path(self.report_path)
        if path.is_file():
            for line in path.read_text(encoding="utf-8").splitlines()[-30:]:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        rows = "".join("<tr><td>" + html.escape(str(e.get("timestamp_utc", ""))) +
                       "</td><td>" + str(len(e.get("alerts", []))) + "</td></tr>" for e in reversed(entries))
        body = ("<!doctype html><html><head><meta charset='utf-8'><title>CryptoShield Local Dashboard</title>"
                "<style>body{font:16px system-ui;max-width:800px;margin:3em auto;padding:1em;background:#101827;color:#e9f0fa}"
                "table{width:100%;border-collapse:collapse}td,th{padding:12px;border-bottom:1px solid #445}</style></head>"
                "<body><h1>KOD3Y CryptoShield</h1><p>Local investigation snapshots. Alerts are not malware verdicts.</p>"
                "<table><tr><th>UTC time</th><th>High-CPU leads</th></tr>" + rows + "</table></body></html>").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="cryptoshield-monitor.jsonl")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    Handler.report_path = args.report
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Local dashboard: http://127.0.0.1:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
