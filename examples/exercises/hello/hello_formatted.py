#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Retrieves and prints command line arguments

In order to explain how to access the command line arguments with Python, this
program will add an optional argument for name, for which it will print an expression
once entered. If no name is entered, World is printed by default.
"""

import argparse


def get_args():
    """Retrieve command line arguments"""

    parser = argparse.ArgumentParser(description='Say Hello!')
    parser.add_argument('-n', '--name', metavar='name (str)', default='World',
                        help='the name to greet, default is World.')

    return parser.parse_args()


def main():
    """Print command line arguments"""

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
