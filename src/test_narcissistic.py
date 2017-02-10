"""Test narcissistic function."""

import pytest

TEST_VARS = [
    [7, True],
    [371, True],
    [122, False],
    [4887, False],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_narc(param, answer):
    """Test narc function."""
    from narcissistic import narcissistic
    assert narcissistic(param) == answer
