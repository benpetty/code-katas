"""Test find_smallest_int function."""


# import sys

# test.assert_equals(findSmallestInt(), )
# test.assert_equals(findSmallestInt(), )
# test.assert_equals(findSmallestInt(), )

import pytest

TEST_VARS = [
    [[78, 56, 232, 12, 11, 43], 11],
    [[78, 56, -2, 12, 8, -33], -33],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_find_smalleset_int(param, answer):
    """Test smallest int function."""
    from find_smallest_int import find_smallest_int
    assert find_smallest_int(param) == answer
