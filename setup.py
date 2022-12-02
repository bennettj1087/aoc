from setuptools import setup, find_packages

setup(
    name="advent-of-code-bennettj1087",
    version="0.1",
    description="bennettj1087's solutions for https://adventofcode.com/",
    url="https://github.com/bennettj1087/aoc",
    author="Justin Bennett",
    author_email="xyz@abc.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["bennettj1087 = aocjmb:mysolve"],
    },
)
