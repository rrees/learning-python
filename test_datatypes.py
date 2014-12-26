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

class TestCollections(unittest.TestCase):
    def test_sets(self):
        spam_set = set(['spam', 'spam', 'spam'])
        self.assertEqual(len(spam_set), 1)

    def test_array_index_access(self):
        breakfast = ['spam', 'beans', 'eggs']
        self.assertEqual(breakfast[0], 'spam')
        self.assertEqual(breakfast[2], 'eggs')
