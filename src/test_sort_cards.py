"""Test sort_cards.py."""


import pytest

TEST_VARS = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')],
]


@pytest.mark.parametrize("param, answer", TEST_VARS)
def test_sort_cards(param, answer):
    """Code wars tests."""
    from sort_cards import sort_cards
    assert sort_cards(param) == answer
