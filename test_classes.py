import unittest

from classes import WordCounter

class TestWordCounter(unittest.TestCase):
    @unittest.skip("implement WordCounter")
    def test_word_counter_count(self):
        word_counter = WordCounter()
        word_counter.count("polly")
        word_counter.count("parrot")
