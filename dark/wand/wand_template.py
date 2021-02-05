##!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Wand: Magic Data Tool for Gryff

Wand uses context to check for and ignore SSL
errors while it scrapes html pages.
"""

import requests
from bs4 import BeautifulSoup


URL = 'https://www.python.org/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
              'signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_content(html):
    s = BeautifulSoup(html, 'html.parser')
    div = s.find('div', {'class': 'medium-widget event-widget last'})
    titles = div.find_all('a')
    return titles


def get_links(s):
    if s.text == 'More':
        return False
    return True


def get_results():
    h = get_html(URL)
    events = get_content(h.text)
    results = list(filter(get_links, events))

    print(URL)
    print('\n')
    for item in results:
        print(item.text)


if __name__ == '__main__':
    get_results()
