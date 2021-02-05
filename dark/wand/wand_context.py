#!/usr/bin/env python3

# Wand - Context Example
#
# Requirements:
#  - beautifulsoup
#
# usage:
#    ./wand_context.py
#
# Copyright: (c) 2021, Rye Miller

"""Wand: Magic Data Tool for Gryff

Wand uses context to check for and ignore SSL
errors while it scrapes html pages.
"""

import urllib.request
import ssl
from bs4 import BeautifulSoup

# ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1011870.html'
html = urllib.request.urlopen(url, context=ctx).read()  # skips through SSL errors

soup = BeautifulSoup(html, 'html.parser')  # parses the table of comments/users

b = 0

print(soup)
tags = soup('span')

for tag in tags:
    print(tag)
    a = int(tag.contents[0])
    print(a)
    b += a
    p = int(tag.text)
    b += p
    print(str(p) + ' + ' + str(b))
print(b)  # shows how many comments total
