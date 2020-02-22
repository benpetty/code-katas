import itertools


def minimum_time(parts):
    """Return minimum possible time to put list of parts together.

    Parts represented by list of numbers representing each part's size.
    Can only combine two parts at a time.
    Time required to combine 2 parts == sum of the parts sizes.
    Size of new part == sum of the parts sizes.
    Repeated until 1 final product

    Example:
    [20, 4, 8, 2] returns 54

    [1, 2, 5, 10, 35, 89] returns 224
    """
    parts.sort()
    return sum(list(itertools.accumulate(parts, lambda x, y: x + y))[1:])
