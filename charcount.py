#!/usr/bin/env python

"""charcount.py: count the number of non-whitespace characters in a text file. Output 
the ten most frequent characters.

Usage: ./charcount.py <file>
"""

from sys import argv, exit

# Potentially clumsy parameter error handling, adapted from
# http://stackoverflow.com/q/14016742
try:
    arg1 = argv[1]
except IndexError:
    print("Usage: charcount.py <file>")
    exit(1)

# Standard Python idiom for reading a file passed as an argument: Using the
# `with` statement automatically closes the file after reading, no matter how
# the nested block exits.
with open(arg1, 'r') as f:
    file_contents = f.read()

# Create a list of characters, excluding whitespace
chars = [c.lower() for c in file_contents if not c.isspace()]
# This doesn't look scalable, but I don't know enough about python to dispute
# it. TODO: implement in itertools and compare timings
char_dict = {c: chars.count(c) for c in chars}

# Remedial python: sort() sorts a list (and only a list!) in-place, whereas
# sorted() accepts any iterable and returns a new list. Print the 10 most
# frequent characters in the input file along with their number of occurrences:
for k, v in sorted(char_dict.items(), key = lambda x: x[1], reverse=True)[:10]:
    print("%s: %s" % (k, v))