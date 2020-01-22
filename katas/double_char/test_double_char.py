"""Test count_code."""

import pytest

TEST_VARS = [
    ['The', 'TThhee'],
    ['AAbb', 'AAAAbbbb'],
    ['Hi-There', 'HHii--TThheerree'],
    ['Word!', 'WWoorrdd!!'],
    ['!!', '!!!!'],
    ['', ''],
    ['a', 'aa'],
    ['.', '..'],
    ['aa', 'aaaa'],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_double_char(param, answer):
    """Test."""
    from .double_char import double_char
    assert double_char(param) == answer
