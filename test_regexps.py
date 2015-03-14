import re
import unittest

class TestRegExpBasics(unittest.TestCase):

	def test_raw_strings(self):

		self.assertEqual('hello', r'hello')

		raw_string = r'\n'
		
		self.assertEqual(len(raw_string), 2)	
		self.assertEqual(raw_string[0], '\\')
		self.assertEqual(raw_string[1], 'n')


	def test_patterns(self):
		s = "dead parrot"

		pattern = re.compile('dead')

		self.assertIsNotNone(pattern.match(s))
		self.assertIsNotNone(re.match(r'dead', s))

		self.assertEqual(pattern.match(s).groups(), re.match(r'dead', s).groups())