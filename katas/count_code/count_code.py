"""String-2 > count_code.

http://codingbat.com/prob/p186048

Return the number of times that the string "code" appears
anywhere in the given string,
except we'll accept any letter for the 'd',
so "cope" and "cooe" count.

count_code('aaacodebbb') -> 1
count_code('codexxcode') -> 2
count_code('cozexxcope') -> 2
"""


def count_code(str):
    """Count code function."""
    count = 0
    try:
        for i in range(len(str)):
            if str[i] == "c" and str[i + 1] == "o" and str[i + 3] == "e":
                count += 1
    except IndexError:
        pass
    return count
