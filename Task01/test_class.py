import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral_triangle():
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 15

def test_isosceles_triangle():
    triangle = Triangle(5, 5, 3)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 13

def test_nonequilateral_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

def test_fractional_sides():
    triangle = Triangle(1.5, 2.5, 3.5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 7.5

def test_large_triangle():
    triangle = Triangle(1000, 1000, 1000)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 3000

def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_violation_of_triangle_inequality():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_small_side_violation():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1e-10, 2, 3)

def test_degenerate_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 2)

def test_all_negative_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, -2, -3)

def test_mixed_invalid_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 0, 3)

def test_non_numeric_sides():
    with pytest.raises(TypeError):
        Triangle("a", 2, 3)

def test_extremely_large_sides():
    triangle = Triangle(1e10, 1e10, 1e10)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 3e10