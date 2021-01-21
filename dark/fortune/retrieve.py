#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

import json

with open('../../data/fortune.json') as f:
    data = json.load(f)

print(json.dumps(data, indent=4, sort_keys=True))

