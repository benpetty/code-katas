"""Regex validate PIN code.

https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

ATM machines allow 4 or 6 digit PIN codes
and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""


def vp(pin):
    """Check if input is a valid int between 4-6 digits."""
    try:
        int(pin)
        length = len(str(pin))
        return length == 4 or length == 6
    except ValueError:
        return False
