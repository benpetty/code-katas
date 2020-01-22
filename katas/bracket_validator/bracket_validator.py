"""

https://www.interviewcake.com/question/python3/bracket-validator

You're working with an intern that keeps coming to you with JavaScript code
that won't run because the braces, brackets, and parentheses are off. To save
you both some time, you decide to write a braces/brackets/parentheses
validator.

Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."

Write an efficient function that tells us whether or not an input string's
openers and closers are properly nested.

Examples:

    "{ [ ] ( ) }" should return True
    "{ [ ( ] ) }" should return False
    "{ [ }" should return False
"""


def is_valid(code):

    BRACKETS = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    OPENERS = set(BRACKETS.keys())
    CLOSERS = set(BRACKETS.values())

    openers_stack = []

    for char in code:

        if char in OPENERS:
            openers_stack.append(char)

        elif char in CLOSERS:

            if not openers_stack:
                return False

            else:

                last_unclosed_opener = openers_stack.pop()

                # If this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning False
                if not BRACKETS[last_unclosed_opener] == char:
                    return False

    return bool(openers_stack == [])
