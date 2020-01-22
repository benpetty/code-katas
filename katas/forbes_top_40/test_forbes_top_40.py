"""Test forbes_top_40."""

import pytest

TEST_VARS = [
    'Phil Knight',
    24400000000,
    'Nike',
    'Mark Zuckerberg',
    44600000000,
    'Facebook',
]


@pytest.mark.parametrize("param", TEST_VARS)
def test_forbes_top_40(param):
    """Function should return the test vars."""
    from .forbes_top_40 import forbes
    assert param in forbes()
