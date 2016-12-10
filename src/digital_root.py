"""Sum of Digits / Digital Root (6 kyu).

In this kata, you must create a digital root function.
A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n.
If that value has two digits,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
"""


def digital_root(n):
    """Sum of digital room."""
    if len(list(str(n))) > 1:
        n = digital_root(sum(map(int, list(str(n)))))
    return n
