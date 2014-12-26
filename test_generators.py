import unittest

class TestGeneratorCode(unittest.TestCase):
    def test_range(self):
        self.assertEqual(range(3), [0,1,2])
