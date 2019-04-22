import pytest


@pytest.mark.parametrize('param, answer', [
    [[20, 4, 8, 2], 54],
    [[1, 2, 5, 10, 35, 89], 224],
])
def test_multiply(param, answer):
    from .minimum_time import minimum_time
    assert minimum_time(param) == answer
