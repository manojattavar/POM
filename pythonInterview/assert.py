
import unittest

class test(unittest.TestCase):
    def testa(self):
        test1 = "test1"
        test2 = "test"

        self.assertEqual(test1, test2)

test().testa()