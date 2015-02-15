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

    def test_functions_in_comprehensions(self):
    	def sentence_case(s):
    		return s[0].upper() + s[1:]

    	self.assertSequenceEqual([sentence_case(tree) for tree in ['elm', 'pine']], ['Elm', 'Pine'])

    def test_functions_in_map(self):
    	pass

    def test_functions_in_reduce(self):
    	pass
