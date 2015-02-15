import unittest

class TestLambdas(unittest.TestCase):
    def test_lambdas_are_functions(self):
    	f = lambda x: x * 2
    	self.assertEqual(f(2), 4)

    def test_lambdas_can_be_used_in_map(self):
    	result = [0, 2, 4]
    	self.assertSequenceEqual(map(lambda x: x * 2, range(3)), result)

    def  test_lambdas_cand_be_used_in_reduce(self):
    	self.assertEqual(reduce(lambda x, y: x + y, range(3)), 3)