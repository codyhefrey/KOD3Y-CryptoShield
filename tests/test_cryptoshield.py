import unittest
from unittest.mock import patch
import cryptoshield

class TestTriage(unittest.TestCase):
    def test_report_has_timestamp_and_sections(self):
        with patch.object(cryptoshield, "processes", return_value={"items": []}), patch.object(cryptoshield, "docker_containers", return_value={"available": False, "items": []}):
            result = cryptoshield.collect()
        self.assertIn("timestamp_utc", result)
        self.assertIn("docker", result)
        self.assertIn("processes", result)

    def test_docker_unavailable_is_not_crash(self):
        with patch("cryptoshield.subprocess.run", side_effect=FileNotFoundError):
            result = cryptoshield.docker_containers()
        self.assertFalse(result["available"])

if __name__ == "__main__":
    unittest.main()
