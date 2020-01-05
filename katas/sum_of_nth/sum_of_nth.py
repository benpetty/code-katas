"""Sum of the first nth term of Series.

https://www.codewars.com/kata/555eded1ad94b00403000071

###Task:

Your task is to write a function which returns the sum of following series
upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

###Rules:

You need to round the answer upto 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.

###Examples:

SeriesSum(1) => 1 = "1"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
NOTE: In PHP the function is called series_sum().
"""


def series_sum(n):
    """Return the sum of the series up to nth term(parameter)."""
    answer = float(0)
    nth = float(1)
    print(nth)
    while n > 1:
        nth += 3
        print("nth: ", nth)
        answer += (1 / nth)
        print('answer :', answer)
        n -= 1
        print("n :", n)
    if n == 1:
        answer += 1
        print("answer: ", answer)
    return str("{0:.2f}".format(answer))
