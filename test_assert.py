import unittest

class TestAssertStatement(unittest.TestCase):

	def test_assert_conditions(self):
		assert True

	def test_assertion_exception(self):

		with self.assertRaises(AssertionError):
			assert False, "This message explains the assertion"