import unittest

class TestGeneratorCode(unittest.TestCase):
    def test_range(self):
        # Range generates numbers starting at zero to match Python's indexing
        self.assertEqual(range(3), [0,1,2])
