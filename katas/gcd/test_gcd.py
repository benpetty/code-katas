import pytest


@pytest.mark.parametrize('param1, param2, answer', [
    [10, 20, 10],
    [2, 4, 2],
    [5, 10, 5],
    [3, 4, 1],
    [0, 0, 0],
    [461952, 116298, 18],
    [7966496, 314080416, 32],
    [24826148, 45296490, 526],
    [12, 0, 12],
    [0, 9, 9],
])
def test_gcd(param1, param2, answer):
    """
    Test gcd returns greatest common division.
    """
    from .gcd import gcd
    assert gcd(param1, param2) == answer

@pytest.mark.parametrize('param, answer', [
    [[5, 10, 15, 20], 5],
    [[2, 4, 6, 8, 10, 20], 2],
    [[1, 2, 3, 4, 5], 1],
    [[0, 0, 0, 0, 0], 0],
    [[200, 600, 900], 100],
    [[1], 1],
])
def test_gcd_spread(param, answer):
    """
    Test gcd_spread returns greatest common division of array.
    """
    from .gcd import gcd_spread
    assert gcd_spread(param) == answer
