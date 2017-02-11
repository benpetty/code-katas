"""Test validate_pin function."""

import pytest

TEST_VARS = [
    ["1", False],
    ["12", False],
    ["123", False],
    ["12345", False],
    ["1234567", False],
    ["1234", True],
    ["1.234", False],
    ["00000000", False],
    ["a234", False],
    [".234", False],
    ["1234", True],
    ["0000", True],
    ["1111", True],
    ["123456", True],
    ["098765", True],
    ["000000", True],
    ["123456", True],
    ["090909", True],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_validate_pin(param, answer):
    """Test validate pin."""
    from validate_pin import vp
    assert vp(param) == answer
