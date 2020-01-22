"""

https://www.interviewcake.com/question/python3/reverse-string-in-place?course=fc1&section=array-and-string-manipulation


Write a function that takes a list of characters and reverses the letters in
place.

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. Since
we're modifying the input, we need a mutable type like a list, instead of
Python 3.6's immutable strings.

"""

def reverse(list_of_chars):
    """

    Complexity:
        O(n) time and O(1) space.

    """

    left  = 0
    right = len(list_of_chars) - 1

    while left < right:
        list_of_chars[left], list_of_chars[right] = \
            list_of_chars[right], list_of_chars[left]
        left += 1
        right -= 1
