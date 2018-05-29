import unittest

def slug(x):
    return x

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(slug('h ello & h,i'), 4)
