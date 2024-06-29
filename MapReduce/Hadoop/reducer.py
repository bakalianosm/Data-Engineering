#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
word_counts= {'han': 0, 'hon': 0, 'den': 0, 'det': 0, 'denna': 0, 'denne': 0, 'hen': 0}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # Increment respective count based on word
    if word in word_counts:
        word_counts[word] += count

# Output the final counts
for word, count in word_counts.items():
    print(f'{word}\t{count}')
