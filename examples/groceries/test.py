#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Tests for a grocery list."""

import os
from subprocess import getoutput
from subprocess import getstatusoutput

file = './grocery.py'


def test_exists():
    """Test if the file exists or not."""

    assert os.path.isfile(file)


def test_usage():
    """Test usage of the program."""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput(f'{file} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


def test_one():
    """Test a single item."""

    out = getoutput(f'{file} cigarettes')
    assert out.strip() == 'Added cigarettes to the list.'


def test_two():
    """Test two items."""

    out = getoutput(f'{file} cigarettes "red bull"')
    assert out.strip() == 'Added cigarettes and red bull to the list.'


def test_two_sorted():
    """Test two items with sorted output."""

    out = getoutput(f'{file} -s pizza cigarettes')
    assert out.strip() == 'Added cigarettes and pizza to the list.'


def test_multiple():
    """Test multiple items."""

    arg = 'cigarettes "red bull" pizza doughnuts'
    out = getoutput(f'{file} {arg}')
    expected = 'Added cigarettes, red bull, pizza, and doughnuts to the list.'
    assert out.strip() == expected


def test_multiple_sorted():
    """Test multiple items with the output sorted."""

    arg = '"red bull" pizza doughnuts cigarettes'
    out = getoutput(f'{file} {arg} --sorted')
    expected = 'Added cigarettes, doughnuts, pizza, and red bull to the list.'
    assert out.strip() == expected
