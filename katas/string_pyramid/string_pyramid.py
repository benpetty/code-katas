"""String pyramid.

https://www.codewars.com/kata/5797d1a9c38ec2de1f00017b

This pyramid should be built from characters from a given string.

You have to create the code for these four methods:
characters = 'abc'
-------------------------------------------------------------------------------
def watch_pyramid_from_the_side(characters):
# shows the pyramid as you would see from the side.

  c
 bbb
aaaaa

def watch_pyramid_from_above(characters):
# shows the pyramid as you would see from above.

aaaaa
abbba
abcba
abbba
aaaaa

def count_visible_characters_of_the_pyramid(characters):
# should return the count of all characters
# that are visible from outside the pyramid.

25

def count_all_characters_of_the_pyramid(characters):
# should count all characters of the pyramid.
# the pyramid is completely solid and has no holes or rooms in it.

35
-------------------------------------------------------------------------------

Every character will be used for building one layer of the pyramid.
So the length of the given string will be the height of the pyramid.
Every layer will be built with stones from the given character.
There is no limit of stones.
The pyramid should have perfect angles of 45 degrees.
There is no meaning in the order or the choice of the characters.
It should work the same for example "aaaaa" or "54321".
Hint: Your output for the side must always be a rectangle!
So spaces at the end of a line must not be deleted or trimmed!
If the string is null or empty,
    you should exactly return this value for the watch-methods
    and -1 for the count-methods.
"""


def watch_pyramid_from_the_side(characters):
    """Show the pyramid as you would see from the side."""
    if characters == "":
        return ""
    elif characters:
        result = []
        spaces = 0
        count = len(characters)
        for char in characters:
            row = (" " * spaces) + (char * (count * 2 - 1)) + (" " * spaces)
            result.append(row)
            spaces += 1
            count -= 1
        return "\n".join(reversed(result))
    return None


def watch_pyramid_from_above(characters):
    """Show the pyramid as you would see from above."""
    if characters == "":
        return ""
    elif characters:
        result = []
        size = len(characters)
        for i in range(size):
            row = characters[:i] + characters[i] * len(characters[i:])
            result.append(row)
            result[i] += result[i][-2::-1]
        for i in range(size - 2, -1, -1):
            result.append(result[i])
        return "\n".join(result)
    return None


def count_visible_characters_of_the_pyramid(characters):
    """Return the count of all visible characters."""
    if characters:
        count = (2 * len(characters) - 1) ** 2
        return count
    return -1


def count_all_characters_of_the_pyramid(characters):
    """Return count of all characters of the pyramid."""
    if characters:
        count = 0
        for i in range(len(characters)):
            count += count_visible_characters_of_the_pyramid(characters[i:])
        return count
    return -1
