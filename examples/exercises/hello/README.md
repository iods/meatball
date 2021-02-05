Hello World
===========

In the beginning, there was "Hello World."

Getting Started
---------------

### Installation

Ensure the python virtual environment has been installed in the correct os.


Exercises
---------

### Instructions

  1. Write a program that outputs "Hello, World!"
```sh
python hello.py

Hello, World!
````
  2. Have that program accept a name as an optional parameter
```sh
python hello.py --name Jack Skellington
Hello, Jack Skellington!
```
  3. Have that program produce help documentation
     ``
     python hello.py -h

     usage: hello.py `[-h]` `[-n str]`

     Say Hello!

     optional arguments:
       -h, --help show this help message and exit
       -n str, --name str the name to greet, default is world.
     ``

Tests
-----

A Makefile includes the needed commands for testing. A successful testing suite should produce the following:

```sh
make test

meatball/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/username/hello
collected 5 items

test.py::test_exists PASSED                                                                                    [ 20%]
test.py::test_runs PASSED                                                                                      [ 40%]
test.py::test_executes PASSED                                                                                  [ 60%]
test.py::test_use PASSED                                                                                       [ 80%]
test.py::test_input PASSED                                                                                     [100%]

================================================= 5 passed in 0.08s ==================================================
```

