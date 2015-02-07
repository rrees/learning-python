import unittest

import comprehensions

class TestGeneratorCode(unittest.TestCase):
    def test_range(self):
        # Range generates numbers starting at zero to match Python's indexing
        self.assertEqual(range(3), [0,1,2])

    def test_generator_syntax(self):
        self.assertSequenceEqual([0, 2, 4, 6], [i * 2 for i in range(4)])

    def test_set_generator_syntax(self):
        self.assertSequenceEqual({1}, {i for i in [1,1,1]})

    def test_dictionary_generator_syntax(self):
        self.assertDictEqual({"a" : 2, "b": 3}, {key: value + 1 for key, value in {"a": 1, "b": 2}.items()})

class TestCreatingGenerators(unittest.TestCase):
    @unittest.skip("implement comprehensions module")
    def test_creating_numbers(self):
        self.assertSequenceEqual(comprehensions.generate_numbers(10),
            [0,1,2,3,4,5,6,7,8,9])

    @unittest.skip("implement comprehensions module")
    def test_creating_natural_numbers(self):
        self.assertSequenceEqual(comprehensions.generate_natural_numbers(10),
            [1,2,3,4,5,6,7,8,9,10])

    @unittest.skip("implement comprehensions module")
    def test_creating_even_numbers(self):
        self.assertSequenceEqual(comprehensions.generate_even_numbers(10),
            [2,4,6,8,10])

    @unittest.skip("implement comprehensions module")
    def test_creating_even_numbers(self):
        self.assertSequenceEqual(comprehensions.generate_even_numbers(10),
            [2,4,6,8,10])
