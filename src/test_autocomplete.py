"""Test autocomplete kata."""

import pytest

vocab = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']

TEST_VARS = [
    [vocab, 4, 'f', ['fix', 'fax', 'fit', 'fist']],
    [vocab, 4, 'fi', ['fix', 'fit', 'fist', 'finch']],
    [vocab, 4, 'fin', ['finch', 'final', 'finial']],
    [vocab, 4, 'finally', []],
    [vocab, 4, 4, 'You must enter a valid string'],
    [vocab, 1, 'f', ['fix']],
    [vocab, 7, 'f', ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final']],
]


@pytest.mark.parametrize("vocab, max_completions, input, answer", TEST_VARS)
def test_autocompleter(vocab, max_completions, input, answer):
    """Test."""
    from autocomplete import AutoCompleter
    complete_me = AutoCompleter(vocab, max_completions=max_completions)
    assert complete_me(input) == answer
