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

	def test_substitution(self):

		start_string = 'dead parrot'
		end_string = 'live parrot'

		self.assertEqual(start_string.replace('dead', 'live'), end_string)
		self.assertEqual(re.sub(r'dead', 'live', start_string), end_string)

		self.assertEqual(start_string.replace('dead', 'live'), re.sub('dead', 'live', start_string))

	def  test_advanced_substitution(self):

		s = 'Polly! Polly Parrot!'

		self.assertEqual(s.replace('Polly', 'Hey'), 'Hey! Hey Parrot!')

		self.assertEqual(re.sub(r'^Polly', 'Hey', s), 'Hey! Polly Parrot!')