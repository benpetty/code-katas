"""Test highest_and_lowest function."""

import pytest

TEST_VARS = [
    ["4 5 29 54 4 0 -214 542 -64 1 -3 6 -6", "542 -214"],
    ["1 -1", "1 -1"],
    ["1 1", "1 1"],
    ["-1 -1", "-1 -1"],
    ["1 -1 0", "1 -1"],
    ["1 1 0", "1 0"],
    ["-1 -1 0", "0 -1"],
    ["42", "42 42"],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_highest_and_lowest(param, answer):
    """Test smallest int function."""
    from highest_and_lowest import high_and_low
    assert high_and_low(param) == answer
