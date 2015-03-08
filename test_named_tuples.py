import unittest

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])



class TestNamedTuples(unittest.TestCase):
    def test_named_tuples(self):
    	p = Point(2,3)

    	self.assertEqual(p.x, 2)
    	self.assertEqual(p.y, 3)

    def test_named_tuples_are_immutable(self):

    	p = Point(5, 8)

        with self.assertRaises(AttributeError):
            p.b = 3

        with self.assertRaises(AttributeError):
            p.x = 7