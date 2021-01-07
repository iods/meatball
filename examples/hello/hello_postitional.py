#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Say Hello!')
parser.add_argument('name', help='the name to greet, default is world.')
args = parser.parse_args()

print('Hello, ' + args.name + '!')
