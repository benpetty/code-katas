"""Test sum_of_nth."""


import pytest

TEST_VARS = [
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_sum_of_nth(param, answer):
    """Code wars tests."""
    from .sum_of_nth import series_sum
    assert series_sum(param) == answer
