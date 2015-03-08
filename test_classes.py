import unittest

from classes import WordCounter

class TestWordCounter(unittest.TestCase):
    @unittest.skip("implement WordCounter")
    def test_word_counter_count(self):
        word_counter = WordCounter()
        word_counter.count("polly")
        word_counter.count("parrot")

        self.assertEquals(word_counter.count(), 2)
        self.assertEquals(word_counter.count(word="polly"), 1)
        self.assertEquals(word_counter.count(word="parrot"), 1)

    @unittest.skip("check that the count tracks dupes correctly")
    def test_word_counter(self):
        word_counter = WordCounter()

        for i in range(3):
            word_counter.count("spam")

        self.assertEquals(word_counter.count(), 3)
        self.assertEquals(word_counter.count(word="spam"), 3)

class Knight:

    def rank(self):
        return 'Knight'

    def wound(self):
        return "Ow!"

class BlackKnight(Knight):
    def wound(self):
        return "It's only a flesh wound"

class TestInheritence(unittest.TestCase):
    def setUp(self):
        self.arthur = Knight()
        self.black_knight = BlackKnight()

    def test_method_overriding(self):
        self.assertEqual(self.arthur.wound(), 'Ow!')
        self.assertEqual(self.black_knight.wound(), "It's only a flesh wound")

    def test_method_inheritence(self):
        self.assertEqual(self.arthur.rank(), self.black_knight.rank())
        self.assertEqual(self.arthur.rank(), 'Knight')
        self.assertEqual(self.black_knight.rank(), 'Knight')

class TestClassMethods(unittest.TestCase):
    def test_class_methods(self):
        class A:
            def __init__(self, x):
                self.x = x

            @classmethod
            def class_method(cls):
                return 'class_method'

            @classmethod
            def add(cls, y):
                return cls(y).x + 1

            @staticmethod
            def static_method():
                return 'static'

        class B(A):
            pass

        b = B(3)

        self.assertEqual(b.x, 3)

        self.assertEqual(b.class_method(), 'class_method')
        self.assertEqual(b.add(5), 6)

        self.assertEqual(b.static_method(), 'static')

class TestCapiClient(unittest.TestCase):
    # CAPI has two endpoints: /search and /content_id
    # Each endpoint takes common parameters: page-size, api-key
    # Using test-driven development;
    # create a class hierarchy that creates appropriate url strings for each endpoint
    # but whose parameter handling is shared
    pass
