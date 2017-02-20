#!/usr/bin/env python

"""charcount.py: create a histogram of character occurrences in a text file.

Usage: ./charcount.py <file>
"""

from sys import argv, exit

# Potentially clumsy parameter error handling, adapted from
# http://stackoverflow.com/questions/14016742/detect-and-print-if-no-command-line-argument-is-provided

try:
    arg1 = argv[1]
except IndexError:
    print "Usage: charcount.py <file>"
    exit(1)

# Standard Python method for reading a file passed as an argument:
# Using the with statement automatically closes the file after reading,
# no matter how the nested block exits.
with open(arg1, 'r') as f:
    file_contents = f.read()

# Create a list of characters, excluding whitespace:
chars = [c.lower() for c in file_contents if not c.isspace()]

nc = len(chars)

char_dict = {c: chars.count(c) for c in chars}

# Recall that sort() sorts a list (and only a list) in-place, whereas
# sorted() accepts any iterable and returns a new list.
# iterable.
# The sort() and sorted() "key" parameter expects a *function* to be called
# on each element of the input list or iterable before making comparisons!
# Super useful, as follows.
# Iterate through the 10 most frequent characters in the input file:
for k, v in sorted(char_dict.items(), key = lambda x: x[1], reverse=True)[:10]:
    print "%s: %s" % (k, v)
