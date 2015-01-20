import unittest

import generators

class TestGenerators(unittest.TestCase):
    def test_fib_generation(self):
        fib = generators.fib()
        first_fibs = [fib.next() for i in range(3)]
        self.assertSequenceEqual(first_fibs, [0,1,1])
