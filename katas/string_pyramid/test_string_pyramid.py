"""Tests for string pyramid kata."""


import pytest


TESTS = [
    [None, None, None, -1, -1],
    ["", "", "", -1, -1],
    [".", ".", ".", 1, 1],
    [".+", " + \n...", "...\n.+.\n...", 9, 10],
    [
        ".+:",
        "  :  \n +++ \n.....",
        ".....\n.+++.\n.+:+.\n.+++.\n.....",
        25,
        35,
    ],
    [
        ".+:#@",
        "    @    \n   ###   \n  :::::  \n +++++++ \n.........",
        (".........\n.+++++++.\n.+:::::+.\n.+:###:+.\n" +
         ".+:#@#:+.\n.+:###:+.\n.+:::::+.\n.+++++++.\n........."),
        81,
        165,
    ],
    [
        'abcdefghijklmnopqrstuvwxyz',
        ('                         z                         \n' +
         '                        yyy                        \n' +
         '                       xxxxx                       \n' +
         '                      wwwwwww                      \n' +
         '                     vvvvvvvvv                     \n' +
         '                    uuuuuuuuuuu                    \n' +
         '                   ttttttttttttt                   \n' +
         '                  sssssssssssssss                  \n' +
         '                 rrrrrrrrrrrrrrrrr                 \n' +
         '                qqqqqqqqqqqqqqqqqqq                \n' +
         '               ppppppppppppppppppppp               \n' +
         '              ooooooooooooooooooooooo              \n' +
         '             nnnnnnnnnnnnnnnnnnnnnnnnn             \n' +
         '            mmmmmmmmmmmmmmmmmmmmmmmmmmm            \n' +
         '           lllllllllllllllllllllllllllll           \n' +
         '          kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          \n' +
         '         jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj         \n' +
         '        iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii        \n' +
         '       hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh       \n' +
         '      ggggggggggggggggggggggggggggggggggggggg      \n' +
         '     fffffffffffffffffffffffffffffffffffffffff     \n' +
         '    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee    \n' +
         '   ddddddddddddddddddddddddddddddddddddddddddddd   \n' +
         '  ccccccccccccccccccccccccccccccccccccccccccccccc  \n' +
         ' bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb \n' +
         'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),

        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n' +
         'abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba\n' +
         'abcccccccccccccccccccccccccccccccccccccccccccccccba\n' +
         'abcdddddddddddddddddddddddddddddddddddddddddddddcba\n' +
         'abcdeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedcba\n' +
         'abcdefffffffffffffffffffffffffffffffffffffffffedcba\n' +
         'abcdefgggggggggggggggggggggggggggggggggggggggfedcba\n' +
         'abcdefghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhgfedcba\n' +
         'abcdefghiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiihgfedcba\n' +
         'abcdefghijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjihgfedcba\n' +
         'abcdefghijkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjihgfedcba\n' +
         'abcdefghijklllllllllllllllllllllllllllllkjihgfedcba\n' +
         'abcdefghijklmmmmmmmmmmmmmmmmmmmmmmmmmmmlkjihgfedcba\n' +
         'abcdefghijklmnnnnnnnnnnnnnnnnnnnnnnnnnmlkjihgfedcba\n' +
         'abcdefghijklmnooooooooooooooooooooooonmlkjihgfedcba\n' +
         'abcdefghijklmnoppppppppppppppppppppponmlkjihgfedcba\n' +
         'abcdefghijklmnopqqqqqqqqqqqqqqqqqqqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrrrrrrrrrrrrrrrrrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrsssssssssssssssrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstttttttttttttsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuuuuuuuuuuutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvvvvvvvvvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwwwwwwwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwxxxxxwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwxyyyxwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwxyyyxwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwxxxxxwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvwwwwwwwvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuvvvvvvvvvutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstuuuuuuuuuuutsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrstttttttttttttsrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrsssssssssssssssrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqrrrrrrrrrrrrrrrrrqponmlkjihgfedcba\n' +
         'abcdefghijklmnopqqqqqqqqqqqqqqqqqqqponmlkjihgfedcba\n' +
         'abcdefghijklmnoppppppppppppppppppppponmlkjihgfedcba\n' +
         'abcdefghijklmnooooooooooooooooooooooonmlkjihgfedcba\n' +
         'abcdefghijklmnnnnnnnnnnnnnnnnnnnnnnnnnmlkjihgfedcba\n' +
         'abcdefghijklmmmmmmmmmmmmmmmmmmmmmmmmmmmlkjihgfedcba\n' +
         'abcdefghijklllllllllllllllllllllllllllllkjihgfedcba\n' +
         'abcdefghijkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjihgfedcba\n' +
         'abcdefghijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjihgfedcba\n' +
         'abcdefghiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiihgfedcba\n' +
         'abcdefghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhgfedcba\n' +
         'abcdefgggggggggggggggggggggggggggggggggggggggfedcba\n' +
         'abcdefffffffffffffffffffffffffffffffffffffffffedcba\n' +
         'abcdeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedcba\n' +
         'abcdddddddddddddddddddddddddddddddddddddddddddddcba\n' +
         'abcccccccccccccccccccccccccccccccccccccccccccccccba\n' +
         'abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba\n' +
         'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),

        2601,
        23426,
    ],
]


@pytest.mark.parametrize(
    "arg, side_view, top_view, count_seen, count_all", TESTS)
def test_pyramid_side_view(arg, side_view, top_view, count_seen, count_all):
    """."""
    from .string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(arg) == side_view


@pytest.mark.parametrize(
    "arg, side_view, top_view, count_seen, count_all", TESTS)
def test_pyramid_top_view(arg, side_view, top_view, count_seen, count_all):
    """."""
    from .string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(arg) == top_view


@pytest.mark.parametrize(
    "arg, side_view, top_view, count_seen, count_all", TESTS)
def test_pyramid_count_seen(arg, side_view, top_view, count_seen, count_all):
    """."""
    from .string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(arg) == count_seen


@pytest.mark.parametrize(
    "arg, side_view, top_view, count_seen, count_all", TESTS)
def test_pyramid_count(arg, side_view, top_view, count_seen, count_all):
    """."""
    from .string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(arg) == count_all
