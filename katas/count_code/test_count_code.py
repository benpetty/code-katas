"""Test count_code."""

import pytest

TEST_VARS = [
    ['aaacodebbb', 1],
    ['codexxcode', 2],
    ['cozexxcope', 2],
    ['cozfxxcope', 1],
    ['xxcozeyycop', 1],
    ['cozcop', 0],
    ['abcxyz', 0],
    ['code', 1],
    ['ode', 0],
    ['c', 0],
    ['AAcodeBBcoleCCccoreDD', 3],
    ['AAcodeBBcoleCCccorfDD', 2],
    ['coAcodeBcoleccoreDD', 3],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_count_code(param, answer):
    """Test."""
    from .count_code import count_code
    assert count_code(param) == answer
