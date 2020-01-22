"""Sort Cards.

https://www.codewars.com/kata/56f399b59821793533000683

Write a function sort_cards() that sorts a shuffled list of cards,
so that any given list of cards is sorted by rank,
no matter the starting collection.

All cards in the list are represented as strings,
so that sorted list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

>>> sort_cards(
    ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']

    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Hint: Tests will have many occurrences of same rank cards,
as well as vary in length. You can assume though,
that input list is always going to have at least 1 element.
"""


def sort_cards(cards):
    """Input a list of strings representing cards and return them sorted."""
    rank = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
            '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
    ranked = []
    for card in cards:
        card = str(card).upper()
        if card in rank:
            card = (rank[card], card)
            ranked.append(card)
    ranked = sorted(ranked)
    result = []
    for card in ranked:
        result.append(card[1])
    return result
