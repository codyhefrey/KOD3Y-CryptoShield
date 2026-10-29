import unittest
from monitor import assess

class MonitorTests(unittest.TestCase):
    def test_alert(self):
        report = {"processes": {"items": [{"pid": 42, "name": "example", "cpu_percent": 95}]}}
        self.assertEqual(assess(report, 80)[0]["type"], "high_cpu")
    def test_no_alert(self):
        self.assertEqual(assess({"processes": {"items": [{"pid": 42, "cpu_percent": 10}]}}, 80), [])

if __name__ == "__main__":
    unittest.main()
