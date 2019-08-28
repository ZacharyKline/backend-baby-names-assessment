#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Finished with some help from Stu


Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# Okay so I need to get the year, then the baby name in alphabetical order, then the ranking of the name.
# Maybe use a for loop to go through the file content and find each thing I need?
def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    solution = []
    names = ''
    popularity = ''
    names_dict = {}
    f = open(filename, 'rU')
    text = f.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    babe_name = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for names in babe_name:
        rank, boy, girl = names
        if boy not in names_dict:
            names_dict[boy] = rank
        if girl not in names_dict:
            names_dict[girl] = rank
    sorted_names = sorted(names_dict)

    for names in sorted_names:
        solution.append('{} {}'.format(names, names_dict[names]))
    solution.insert(0, year.group(1))
    return solution


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser(description='Search for the most popular baby name rankings in each year')
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files
    create_summary = args.summaryfile

    if create_summary:
        for filename in file_list:
            years = extract_names(filename)
            print_out = '\n'.join(years)+'\n'
            with open(filename + '.summary', 'w') as f:
                f.write(print_out)
    else:
        for filename in file_list:
            years = extract_names(filename)
            print(years)
    # option flag
    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
if __name__ == '__main__':
    main()
