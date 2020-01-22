# -*- coding: utf-8 -*-
"""Python Practice: Autocomplete.

A common feature in websites is “autocomplete”.
Typically, a user is entering input into a form field,
and the system provides a list of suggested completions.
Each new character typed reduces the list of suggestions.
The completions are typically drawn from a vocabulary of available values.
If the user is typing a sequence
that is not matched in the list of available values,
no completions are suggested.

Your Task ------------------------------------------------------------------- #
Write a callable Python class which will implement autocomplete functionality.
Your class should take a list of words
to be a vocabulary as an argument on initialization.
It should also accept a max_completions argument,
which controls the maximum number of suggested completions for a given string.
The max_completions argument should default to 5.

The input to the call method for the class
will be the string the user has typed.
When called, this class should return a list
of at most max_completions suggested words.
If there are more available completions than allowed,
you are free to decide which to return.
If there are no completions available,
you should return an empty list.
Your class should handle inappropriate inputs correctly.

In the end, your class should be usable like so:

>>> from autocomplete import AutoCompleter
>>> vocabulary = [
        'fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
>>> complete_me = AutoCompleter(vocabulary, max_completions=4)
>>> complete_me('f')
['fix', 'fax', 'fit', 'fist']

>>> complete_me('fi')
['fix', 'fit', 'fist', 'finch']

>>> complete_me('fin')
['finch', 'final', 'finial']

>>> complete_me('finally')
[]

Stretch Goal----------------------------------------------------------------- #
Update the __init__ method of your class
to accept a filename instead of a list.
If the provided value is a list, then operate as before.
If it is a file, then the vocabulary should be read from the file.
You may assume that the file is formatted with one word per line.
You may assume that there are no blank lines in the file.
You may not assume that there is no extra whitespace on any line.
"""


class AutoCompleter(object):
    """."""

    def __init__(self, vocab, max_completions=5):
        """Create an instance of AutoCompleter class."""
        self.vocab = [str(each) for each in vocab]
        self.max_completions = int(max_completions)

    def __call__(self, complete_me):
        """."""
        if isinstance(complete_me, str):
            suggestions = []
            for word in self.vocab:
                if len(suggestions) >= self.max_completions:
                    break
                if complete_me in word:
                    suggestions.append(word)
        else:
            return 'You must enter a valid string'
        return suggestions
