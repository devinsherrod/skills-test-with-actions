# System Modules
import math
import pytest
# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


from src.calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_negative_radius():
    """Test that negative radius raises ValueError"""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-5)

def test_get_nth_fibonacci_negative_n():
    """Test that negative n raises ValueError"""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)