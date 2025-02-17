import math

class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам его сторон.

    Позитивные тесты:
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    >>> get_triangle_type(5, 5, 3)
    'isosceles'
    >>> get_triangle_type(1.5, 2.5, 3.5)
    'nonequilateral'
    >>> get_triangle_type(10, 10, 10)
    'equilateral'

    Негативные тесты:
    >>> get_triangle_type(0, 4, 5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны треугольника должны быть положительными числами.
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Нарушено неравенство треугольника.
    >>> get_triangle_type(-1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны треугольника должны быть положительными числами.
    >>> get_triangle_type(1e-10, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Нарушено неравенство треугольника.
    >>> get_triangle_type(1, 1, 2)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Нарушено неравенство треугольника.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника")
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()