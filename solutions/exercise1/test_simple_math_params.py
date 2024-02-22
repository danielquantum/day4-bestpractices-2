# test_simple_math_params.py
import simple_math
import pytest

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])

def test_square_parametrized(n, expected):
    assert simple_math.square(n) == expected