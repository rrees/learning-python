import unittest

import generators

class TestGenerators(unittest.TestCase):
    def test_fib_generation(self):
        fib = generators.fib()
        first_fibs = [fib.next() for i in range(3)]
        self.assertSequenceEqual(first_fibs, [0,1,1])

    @unittest.skip("completed in class")
    def test_integer_generation(self):
    	int_gen = generators.my_range(4, 6)

    	self.assertSequenceEqual([i for i in int_gen], [4, 5])