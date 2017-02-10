"""Test forbes_top_40."""


def test_sort_cards(param, answer):
    """Function should return Phil Knight."""
    from forbes_top_40 import forbes
    assert 'Phil Knight' in forbes()
