import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmax_integer(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1,2,3,4]), 4)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([4,3,2,1]), 4)
        self.assertAlmostEqual(max_integer([3,4,2,1]), 4)

if __name__ == '__main__':
    unittest.main()
