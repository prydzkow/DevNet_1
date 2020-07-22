import unittest
from get_greetings import get_hello
from get_greetings import get_good_morning

class TestGetGreetings(unittest.TestCase):

    def test_get_hello(self):
        self.assertEqual(get_hello().upper(), 'HELLO WORLD!')

    def test_get_good_morning(self):
        self.assertEqual(get_good_morning().upper(), 'GOOD MORNING!')

if __name__ == '__main__':
    unittest.main()