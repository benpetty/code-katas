"""Test multiply function."""

import pytest

TEST_VARS = [
    [1, 1, 1],
    [2, 1, 2],
    [2, 2, 4],
    [3, 5, 15],
]


@pytest.mark.parametrize("param1, param2, answer", TEST_VARS)
def test_multiply(param1, param2, answer):
    """Test multiply function."""
    from multiply import multiply
    assert multiply(param1, param2) == answer
