import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestGetTriangleType(unittest.TestCase):
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")

    def test_fractional_sides(self):
        self.assertEqual(get_triangle_type(1.5, 2.5, 3.5), "nonequilateral")

    def test_large_equilateral(self):
        self.assertEqual(get_triangle_type(10, 10, 10), "equilateral")

    def test_invalid_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)

    def test_invalid_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

    def test_invalid_triangle_inequality(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_small_side_violation(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1e-10, 2, 3)

    def test_degenerate_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 2)

if __name__ == "__main__":
    unittest.main()