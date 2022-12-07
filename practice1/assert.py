
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        x = "test1"
        y = "test"

        self.assertEqual(x, y)

TestStringMethods().test_negative()