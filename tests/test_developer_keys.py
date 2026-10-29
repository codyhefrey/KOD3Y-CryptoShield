import tempfile
import unittest
from pathlib import Path
from developer_keys import issue, verify

class DeveloperKeyTests(unittest.TestCase):
    def test_unique_and_verified(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d) / "keys.json"
            first = issue(store)
            second = issue(store)
            self.assertNotEqual(first, second)
            self.assertTrue(verify(first, store))
            self.assertTrue(verify(second, store))
            self.assertFalse(verify(first + "wrong", store))
    def test_missing_registry_rejects(self):
        self.assertFalse(verify("kcs_dev_abc_fake", "missing-file-123.json"))

if __name__ == "__main__":
    unittest.main()
