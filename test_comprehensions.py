import unittest

import comprehensions

class TestComprehensions(unittest.TestCase):
    def test_range(self):
        # Range generates numbers starting at zero to match Python's indexing
        self.assertEqual(range(3), [0,1,2])

    def test_comprehension_immutability(self):
        a = [1,2,3]

        b = [i + 1 for i in a]

        self.assertSequenceEqual(a, [1,2,3])
        self.assertSequenceEqual(b, [2,3,4])

    def test_comprehension_syntax(self):
        self.assertSequenceEqual([0, 2, 4, 6], [i * 2 for i in range(4)])

    def test_set_comprehension_syntax(self):
        self.assertSequenceEqual({1}, {i for i in [1,1,1]})

    def test_dictionary_comprehension_syntax(self):
        self.assertDictEqual({"a" : 2, "b": 3}, {key: value + 1 for key, value in {"a": 1, "b": 2}.items()})

    def test_comprehension_filtering(self):
        self.assertSequenceEqual(["bacon"], [item for item in ["spam", "bacon", "eggs"] if len(item) > 4])

class TestCreatingComprehensions(unittest.TestCase):
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
    def test_creating_even_numbers_via_map_and_filter(self):
        self.assertSequenceEqual(comprehensions.generate_even_numbers_map_and_filter(10),
            [2,4,6,8,10])
