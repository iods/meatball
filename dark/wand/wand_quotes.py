#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Wand: Magic Data Tool for Gryff (Tiffany's <3)

Here wand pulls some life-changing quotes to kick-ass by
and saves them locally to a file.
"""

import os
import requests
from bs4 import BeautifulSoup

FILE = '/bluntsandwisdom.txt'
FOLDER = os.getcwd() + '/quotes'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
              'signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
PATH = FOLDER + FILE
URL = 'https://wisdomquotes.com/life-quotes/'


def get_html(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS).text
    markup = BeautifulSoup(resp, 'html.parser')
    return markup


def get_content_tags(markup: BeautifulSoup) -> list:
    bquote = markup.find_all('blockquote')
    bquote_tags = list(filter(
        lambda blockquote: blockquote.attrs.get('class') != ['blockquote.quotescollection-quote'], bquote))
    return bquote_tags


def get_quotes(bquote_tags: list):
    for quote in bquote_tags:
        yield quote.find('p').get_text('\n')


def save(bquote_tags: list):
    global FOLDER, PATH
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    with open(PATH, 'w') as file:
        for txt in get_quotes(bquote_tags):
            file.write(txt)

    print(f'Bluntz and Wizdom: {PATH}')


if __name__ == '__main__':
    html = get_html(URL)
    tags = get_content_tags(html)

    save(tags)
