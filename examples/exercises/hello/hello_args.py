#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say Hello!')
    parser.add_argument('-n', '--name', metavar='name (str)', default='World',
                        help='the name to greet, default is World.')

    return parser.parse_args()


def main():
    args = get_args()

    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
