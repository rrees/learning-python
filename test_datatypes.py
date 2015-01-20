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

    def test_lists(self):
        spam_list = ['spam', 'spam', 'spam']
        self.assertEqual(len(spam_list), 3)

    def test_list_index_access(self):
        breakfast = ['spam', 'beans', 'eggs']
        self.assertEqual(len(breakfast), 3)
        self.assertEqual(breakfast[0], 'spam')
        self.assertEqual(breakfast[2], 'eggs')

    def test_list_append(self):
        breakfast = []
        breakfast.append('spam')
        self.assertEqual(len(breakfast), 1)

    def test_dictionary_addition(self):
        menu = {'Spam and eggs' : ['spam', 'eggs']}
        self.assertEqual(len(menu.keys()), 1)
        menu['Spam, bacon and eggs'] = ['spam', 'bacon', 'eggs']

    def test_deletion_in_a_list(self):
        breakfast = ['spam', 'beans', 'spam']
        del(breakfast[1])
        self.assertEqual(len(breakfast), 2)

    def test_deletion_in_a_dict(self):
        menu = {'Spam and eggs' : ['spam', 'eggs']}
        del(menu['Spam and eggs'])
        self.assertEqual(len(menu.keys()), 0)

class TestTuples(unittest.TestCase):
    def test_destructuring(self):
        x,y,z = (3,4,5)
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)
        self.assertEqual(z, 5)

class TestBooleanEvaluation(unittest.TestCase):
    def test_numbers(self):
        self.assertFalse(0)
        self.assertTrue(7)

    def test_lists(self):
        self.assertFalse([])
        self.assertTrue([1])

    def test_dictionaries(self):
        self.assertFalse({})
        self.assertTrue({'hello': True})
