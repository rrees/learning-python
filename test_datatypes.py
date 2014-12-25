import unittest

class TestDataTypes(unittest.TestCase):

    def test_number_promotion(self):
        self.assertEqual(3.0 + 4, 7.0)
