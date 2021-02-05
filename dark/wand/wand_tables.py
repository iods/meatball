#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Wand: Magic Data Tool for Gryff

Wand uses context to check for and ignore SSL
errors while it scrapes html pages.
"""

import pandas

url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

tables = pandas.read_html(url)  # returns a list of all tables on a page
print(tables)

which_table = tables[1]
print(which_table)
