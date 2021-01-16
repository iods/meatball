#!/usr/bin/env python3
"""
Tests for Iods Python Hello World.
"""

import os
from subprocess import getoutput
from subprocess import getstatusoutput

filename = "./hello.py"


def test_exists():
    """
    Test if the file exists or not.
    """
    assert os.path.isfile(filename)


def test_runs():
    """
    Test if the file runs with python.
    """
    out = getoutput(f"python {filename}")
    assert out.strip() == "Hello, World!"


def test_executes():
    """
    Test if the file executes a specific action by default.
    """
    out = getoutput(filename)
    assert out.strip() == "Hello, World!"


def test_use():
    """
     Test usage of the program.
    """
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{filename} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


def test_input():
    """
    Test whether the program can take input or not.
    """
    for value in ['Rye', 'Tiffany']:
        for flag in ['-n', '--name']:
            rv, out = getstatusoutput(f'{filename} {flag} {value}')
            assert rv == 0
            assert out.strip() == f'Hello, {value}!'
