"""Setup file for Code Katas repo."""

from setuptools import setup


setup(
    name="code_katas",
    description="My solutions to coding challenges.",
    version=0.1,
    author="Ben Petty",
    author_email="contact@benpetty.me",
    license="MIT",
    py_modules=[
        'autocomplete',
        'count_code',
        'digital_root',
        'double_char',
        'find_smallest_int',
        'forbes_top_40',
        'get_middle',
        'highest_and_lowest',
        'jaden_casing',
        'multiply',
        'narcissistic',
        'sort_cards',
        'sum_of_nth',
        'validate_pin',
        'flight_paths.py',
    ],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={
        'testing': [
            'pytest',
            'pytest-cov',
            'tox',
            'coveralls',
        ]
    }
)
