import unittest
from test import hello

class TestHello(unittest.TestCase):
	def test_hello(self):
		self.assertEqual(hello(), "Hello, Jenkins!")

if __name__ == '__main__':
	unittest.main()
