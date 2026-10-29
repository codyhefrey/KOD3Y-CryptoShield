import unittest
from unittest.mock import patch
from http.server import ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen
import json
from api import Handler

class APITests(unittest.TestCase):
    def test_health(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urlopen("http://127.0.0.1:%d/v1/health" % server.server_port, timeout=3) as response:
                data = json.load(response)
            self.assertEqual(data["status"], "ok")
            self.assertEqual(data["version"], "v1")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)

if __name__ == "__main__":
    unittest.main()
