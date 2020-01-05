"""Get the Middle Character (7 kyu).

https://www.codewars.com/kata/56747fd5cb988479af000028

You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
"""


def get_middle(word):
    """Return the middle character(s) of a string."""
    chopped = list(word)
    if len(word) % 2 == 0:
        return (chopped[int(len(chopped) / 2 - 1)] +
                chopped[int(len(chopped) / 2)])
    elif len(word) % 2 == 1:
        return chopped[int(len(chopped) / 2)]
