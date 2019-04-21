import pytest


@pytest.mark.parametrize('param1, param2, answer', [
    [[0, 1, 0, 1, 0, 0, 1, 1, 0], 25, [1, 0, 0, 0, 1, 1, 1, 1, 1]],
    [[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1], 38, [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0]]
])
def test_gcd(param1, param2, answer):
    """
    Test game_of_thrones.
    """
    from .game_of_thrones import game_of_thrones
    assert game_of_thrones(param1, param2) == answer
