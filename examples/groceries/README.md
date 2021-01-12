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