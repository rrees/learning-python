import unittest

class TestFunctions(unittest.TestCase):
    def test_functions_can_be_declared_at_any_point(self):
    	def f(x):
    		def g(x):
    			return 2 * x

    		return 1 + g(x)

    	self.assertEqual(f(1), 3)
    	self.assertEqual(f(2), 5)

    	for i, result in [(1,3), (2, 5), (3, 7)]:
    		self.assertEqual(f(i), result)

    def test_functions_are_identities(self):

    	def double(n):
    		return n * n

    	def apply_function(f, n):
    		return f(n)

    	self.assertEqual(apply_function(double, 2), 4)