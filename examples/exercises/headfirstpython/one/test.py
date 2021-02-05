#!/usr/bin/env python3
"""
Tests for Head First Python, Chapter 1
"""

import os

filename = "./odd.py"


def test_exists():
    """
    Test whether the file exists or not.
    """
    assert os.path.isfile(filename)

