
def gcd(x, y):
    """
    In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an
    efficient method for computing the greatest common divisor (GCD) of two
    numbers, the largest number that divides both of them without leaving a
    remainder. It is named after the ancient Greek mathematician Euclid, who
    first described it in his Elements (c. 300 BC). It is an example of an
    algorithm, a step-by-step procedure for performing a calculation according
    to well-defined rules, and is one of the oldest algorithms in common use.
    It can be used to reduce fractions to their simplest form, and is a part of
    many other number-theoretic and cryptographic calculations.

    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    while y:
        x, y = y, x % y
    return x


def gcd_spread(arr):
    """Return the greatest common divisor of all numbers in array.

    Args:
        arr (list): List of numbers.

    Returns:
        int: The greatest common divisor.
    """
    try:
        greatest = gcd(arr[0], arr[1])
        for i in range(2, len(arr)):
            greatest = gcd(greatest, arr[i])
        return greatest

    except IndexError:
        return arr[0]
