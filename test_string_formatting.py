import unittest

class TestStringFormatting(unittest.TestCase):
    def test_tuple_substitution(self):
        self.assertEquals("Hello %s" % "World", "Hello World")

    def test_multiple_tuple_substitution(self):
        self.assertEquals("%d %s %s" % (3, "gold", "rings"),
            "3 gold rings")

    def test_format_substitution(self):
        self.assertEquals("Hello {0}".format("World"), "Hello World")

    def test_format_substitution_by_keyword(self):
        self.assertEquals("The {person} went from {place} to {place}".format(person="boy", place="door"),
            "The boy went from door to door")
