import unittest

from pythonfile import is_prime

class Tests(unittest.TestCase):

	def test_1(self):
		"""Kiểm tra với số 1."""
		self.assertFalse(is_prime(1))
	def test_2(self):
		"""Kiểm tra với số 2."""
		self.assertTrue(is_prime(2))
	def test_3(self):
		"""Kiểm tra với số 3."""
		self.assertTrue(is_prime(3))
	def test_11(self):
		"""Kiểm tra với số 11."""
		self.assertTrue(is_prime(11))
	def test_25(self):
		"""Kiểm tra với số 25."""
		self.assertFalse(is_prime(25))
if __name__ == "__main__":
	unittest.main()
