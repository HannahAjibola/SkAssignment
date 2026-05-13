import unittest
from perfectSquare import pSquare

class TestPerfectNumber(unittest.TestCase):

    def test_is_perfect_number(self):
        self.assertTrue(
            pSquare([[2,2], [2,2]]))

    def test_given_example(self):
        self.assertFalse(
            pSquare([
                [10, 4,7],
                [3, 9,9],
                [6, 4,7]
            ])
        )

    def test_3_by_3_array(self):
        self.assertTrue(
            pSquare([
                [8, 1, 6],
                [3, 5, 7],
                [4, 9, 2]
            ])
        )


    def test_negative_numbers(self):
        self.assertTrue(
            pSquare([
                [1, -1],
                [-1, 1]
            ])
        )

    def test_unequal_number(self):
        self.assertFalse(
            pSquare([
                [5, 5, 5],
                [1, 1, 1],
                [2, 2, 2]
            ])
        )
 

    def test_invalid_number(self):
        self.assertFalse(pSquare([[1,2],[3,4]]))

if __name__=="__main__":
    unittest.main()
