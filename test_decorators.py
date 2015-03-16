import unittest

import decorators

class TestDecoration(unittest.TestCase):
    def test_upper_case_example(self):
        self.assertEquals(decorators.greet("world"), 'HELLO WORLD')

    @unittest.skip('Implement the lowercase decorator first')
    def test_lower_case_example(self):
        self.assertEquals(decorators.farewell("world"), 'farewell world')