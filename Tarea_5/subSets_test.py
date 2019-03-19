import unittest
from subSets import count_sets

class subSets_test(unittest.TestCase):
	def test1_count_Sets(self):
		intSet = [2,4,6,10]
		self.assertEqual(count_sets(intSet,16),2)

	def test2_count_Sets(self):
		intSet = [2,3,7,8,10]
		self.assertEqual(count_sets(intSet,11),1)

	def test3_count_Sets(self):
		intSet = [1,2,4,6,8,4,6,7]
		self.assertEqual(count_sets(intSet,30),5)

if __name__ == '__main__':
    unittest.main()