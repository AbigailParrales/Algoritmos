import unittest
from nQueens import N_Queens

class test_nQueens(unittest.TestCase):
	def test1_N_Queens(self):
		answer4_4 = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
		self.assertEqual(N_Queens(4),answer4_4)
	def test2_N_Queens(self):
		answer4_5 = [[1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0]]
		self.assertEqual(N_Queens(5),answer4_5)
	def test3_N_Queens(self):
		answer4_10 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
		self.assertEqual(N_Queens(10),answer4_10)

if __name__ == '__main__':
    unittest.main()