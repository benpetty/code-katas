"""Test digital_root function."""

import pytest

TEST_VARS = [
    [16, 7],
    [195, 6],
    [992, 2],
    [999999999999, 9],
    [167346, 9],
    [0, 0]
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_digital_root(param, answer):
    """Test digital root function."""
    from .digital_root import digital_root
    assert digital_root(param) == answer
