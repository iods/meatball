Groceries
=========

Write a program that will correctly format the items needed at the grocery store by a software developer.


Getting Started
---------------

### Installation

Ensure the python virtual environment has been installed in the correct os.


Exercises
---------

### Instructions

For one item, it should print the following:
```sh
$ ./grocery.py cigarettes
You are going to buy ciggarettes.
```

For two items, place "and" in between:
```sh
$ ./grocery.py pizza ciggarettes
You are going to buy pizza and ciggarettes.
```

For three or more items, use commas and "and":
```sh
$ ./grocery.py pizza cigarettes doughnuts
You are going to buy pizza, ciggarettes, and doughnuts.
```

For the ``--sorted`` flag, sort the items:
```sh
$ ./grocery.py doughnuts "red bull" pizza cigarettes --sorted
You are going to buy ciggarettes, doughnuts, pizza, and red bull.
```

Respond to `-h` and `--help` with longer usage:
```sh
python grocery.py -h --help
usage: grocery.py [-h] [-s] str [str ...]

Grocery list for software developers.

positional arguments:
  str           Item or items to purchase at the grocery store.

optional arguments:
  -h, --help    show this help message and exit
  -s, --sorted  A boolean flag to sort the items. (default: False)
```

Tests
-----

Run the test suite to ensure your program is correct:

```sh
groceries [feature/groceries] ⚡  make test
================================================ test session starts ================================================
platform linux -- Python 3.6.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /home/darkstar/Developer/python/python-meatball/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/darkstar/Developer/python/python-meatball/examples/groceries
collected 7 items

test.py::test_exists PASSED                                                                                   [ 14%]
test.py::test_usage PASSED                                                                                    [ 28%]
test.py::test_one PASSED                                                                                      [ 42%]
test.py::test_two PASSED                                                                                      [ 57%]
test.py::test_two_sorted PASSED                                                                               [ 71%]
test.py::test_multiple PASSED                                                                                 [ 85%]
test.py::test_multiple_sorted PASSED                                                                          [100%]

================================================= 7 passed in 0.25s =================================================
```