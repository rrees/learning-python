import unittest

class TestDataTypes(unittest.TestCase):

    def test_integer_arithmetic(self):
        self.assertEqual(3 + 4, 7)
        
    def test_number_promotion(self):
        self.assertEqual(3.0 + 4, 7.0)

    def test_string_concatenation(self):
        self.assertEqual("hello " + "world", "hello world")

    def test_boolean_literals(self):
        self.assertTrue(True)
        self.assertFalse(False)
