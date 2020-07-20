import unittest
from get_greetings import get_hello

class TestHelloWorld(unittest.TestCase):

    def test_get_hello(self):
        self.assertEqual(get_hello().upper(), 'HELLO WORLD!')

if __name__ == '__main__':
    unittest.main()