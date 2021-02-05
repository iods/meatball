#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

import argparse


def main():
    parser = argparse.ArgumentParser(description='Say Hello!')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='the name to greet, default is World.')

    args = parser.parse_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
