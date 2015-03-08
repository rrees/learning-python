import unittest

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class PointClass:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class TestReflection(unittest.TestCase):
	def setUp(self):
		self.p = Point(9, 15)
		self.pc = PointClass(23, 4)
		self.all = [self.p, self.pc]

	def test_attribute_checking(self):
		for item in self.all:
			self.assertTrue(hasattr(item, 'x'))
			self.assertTrue(hasattr(item, 'y'))

			self.assertFalse(hasattr(item, 'b'))

	def test_attribute_reading(self):
		for item in self.all:
			self.assertEqual(getattr(item, 'x'), item.x)
			self.assertEqual(getattr(item, 'y'), item.y)