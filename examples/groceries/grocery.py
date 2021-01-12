#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""
"""

import argparse


def get_arguments():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Grocery list for software developers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item or items to purchase at the grocery store.')

    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag to sort the items.',
                        action='store_true')

    return parser.parse_args()


def main():
    """Interpret those command-line arguments here."""

    args = get_arguments()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    if num == 1:
        buy = items[0]
    elif num == 2:
        buy = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        buy = ', '.join(items)

    print('You are going to buy {}.'.format(buy))


if __name__ == '__main__':
    main()
