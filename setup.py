from setuptools import setup


setup(
    name="katas",
    description="My solutions to coding challenges.",
    version=0.1,
    author="Ben Petty",
    author_email="benjamin.s.petty@gmail.com",
    license="MIT",
    extras_require={
        'testing': [
            'pytest',
            'pytest-cov',
            'tox',
            'coveralls',
        ]
    }
)
