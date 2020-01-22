"""

https://www.interviewcake.com/question/python3/reverse-words?course=fc1&section=array-and-string-manipulation

You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to
break into a major European National Cake Vault. The message has been mostly
deciphered, but all the words are backward! Your colleagues have handed off the
last step to you.

Write a function reverse_words() that takes a message as a list of characters
and reverses the order of the words in place.

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. Since
we're modifying the message, we need a mutable type like a list, instead of
Python 3.6's immutable strings.

For example:

    message = [ 'c', 'a', 'k', 'e', ' ',
                'p', 'o', 'u', 'n', 'd', ' ',
                's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

When writing your function, assume the message contains only letters and
spaces, and all words are separated by one space.
"""

def reverse_words(message):
    """

    Complexity:
        O(n) time and O(1) space

    """
    num_chars = len(message)
    reverse_characters(message, 0, num_chars - 1)
    current_word_start_index = 0

    for idx in range(num_chars + 1):
        if idx == num_chars or message[idx] == ' ':
            reverse_characters(message, current_word_start_index, idx - 1)
            current_word_start_index = idx + 1


def reverse_characters(message, left, right):
    while left < right:
        message[left], message[right] = \
            message[right], message[left]
        left += 1
        right -= 1
