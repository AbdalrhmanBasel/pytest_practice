import pytest


# Function
def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


test_add_context = [
    (1, 2, 3),
    (2, 4, 6),
    (3, -2, 1),
    ("hello", ' world', 'hello world')
]


# Fixture
@pytest.mark.parametrize('n1, n2, expected', test_add_context)
def test_add(n1, n2, expected):
    assert add(n1, n2) == expected


test_minus_context = [
    (3, 1, 2),
    (-3, 3, -6),
    (0, -1, 1),
]


@pytest.mark.parametrize('n1, n2, expected', test_minus_context)
def test_minus(n1, n2, expected):
    assert minus(n1, n2) == expected
