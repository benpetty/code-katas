"""Test get_middle function."""

import pytest

TEST_VARS = [
    ["test", "es"],
    ["testing", "t"],
    ["middle", "dd"],
    ["A", "A"],
    ["of", "of"],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_get_middle(param, answer):
    """Test get middle function."""
    from .get_middle import get_middle

    assert get_middle(param) == answer
