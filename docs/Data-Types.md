- [Lists](#lists)
  - [Constructing Lists](#constructing-lists)
  - [Accessing Lists](#accessing-lists)
  - [Modifying Lists](#modifying-lists)
  - [Iterating Lists](#iterating-lists)
- [Dictionaries](#dictionaries)


## H2
### H3
#### H4
##### h5
There are four (4) main collection data types in Python, they are:
1. **List** - _A collection which is ordered and changeable (modifiable)._
2. **Dictionary**
3. **Tuple** -
4. **Set**


## Lists

A list is a collection of different data types which is ordered and modifiable (mutable). A list can be empty or it may have different data types or items. Allows duplicate members.


### List vs. Array

Is the data type `['alpha', 'beta']` the same in Python and PHP/JavaScript? Do they even exist in Python?

Short answer, yes.

Similarities for the both include that they are both mutable, can be indexed and iterated through, sliced, and are used for storing data. Arrays are most popular in Data Science and the `numpy` array.

The biggest difference between the two is that lists are containers for elements having differing data types but arrays are used as containers for elements of the same data type.


### Constructing Lists

The first operation for a list in Python is it's creation. There are multiple ways for constructing lists. They are:

#### Basic Construction
To create a list, you can compose elements in `[]` as comma separated values.
```py
data_list = []          # Uses square brackets syntax to init list (empty literal notation)
data_list = ['a', 'b']  # Uses brackets to init w/ comma separated values (literal notation w/ values)
```

#### Slicing
You can also create lists by slicing existing lists, just like strings `[start:stop:step]`.
```py
data_list = ['a', 'b', 'c', 'd']  # The list you are creating from
data_list_new = data_list[1:3]    # Slice the original list, starting from the first index to the third
print(data_list_new)              # Returns a new list with the values ['b', 'c']
```

#### The `list()` Method
Using the Python built-in `list()` function
```py
data_string = 'Alpha'
print(list(data_string))      # Converts a string to a list using `list()` ['A', 'l', 'p', 'h', 'a']

data_number = list(range(6))
print(data_number)            # Converts a `range()` of six numbers [0, 1, 2, 3, 4, 5]

data_tuple = list((3, 6, 9))
print(data_tuple)             # Converts a tuple into a list [3, 6, 9]
```
> The `list()` function expects an iterable which could be a set, dictionary, a tuple, etc.; however, if nothing is passed it will return an empty list.


#### List Comprehension
Beyond the basic construction, list comprehension is a concise way of creating `list` objects using the syntax `[expression for x in iterable if condition]`
```py
data_dict = {'a': 1, 'B': 2, 'c': 3}               # Declare a dictionary as the iterable for list comprehension
data_comp = [x*x for x in data_dict.values()]      # Returns a list with the dictionary's values, squared
data_comp = [x.lower() for x in data_dict.keys()]  # Returns a list with all keys lowercase
data_comp = [list(x) for x in data_dict.items()]   # Returns a list of the items as their own lists
```
> Another information piece of using list comprehension.


### Accessing Lists

#### Indexing and Reverse Indexing

You can access lists using indexing (Python is zero-based) that count from the left starting at `[0]`. You can also use reverse indexing counting from the right
and using `[-1]`. This is beneficial when accessing single items. When counting from the left, the first index is `0` and so on.
```py
data_list = [1, 2, 3, 4, 5]  # Create the list
print(data_list[3])         # Returns the third index in the list (4)
print(data_list[-1])        # Returns the last element in the list (5)
```

#### Unpacking
We can access lists individually or elements within a range.

* Unpacking individual and range of elements
* Slicing
* Random Selection
* Using the Python built-in `index()` function

#### Slicing
Sometimes, we need to work with a subsequence of the original list object. One common way is to use slicing to get some items. There are several variations on how we can slice the list — some common ones are listed in the following code snippet:
```py
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Create the original list
print(data_list[:5])                         # Returns the first five elements (end index is open/not inclusive)
print(data_list[5:])                         # Returns the sixth element to the end (start index is closed/inclusive)
print(data_list[2:9])                        # Returns the third to the ninth element
print(data_list[3:-2])                       # Returns a reverse indexed list
```

### Modifying Lists

A major feature of lists is their mutability. Or the ability to change or remove a value.

#### Remove Elements

There are three ways to remove an element from a list:
* Using the **del** keyword
* Using the `.remove()` method
* Using the `.pop()` method

```py
data_list = ['a, 'b', 'c', 'd', 'e']  # Create the initial list

del data_list[0]                      # Use the del keyword and provide the index to remove a value
print(data_list)                      # Returns the list with the first value removed. ['b', 'c', 'd', 'e']

data_list.remove('b')                 # Removes the first matching element from the list
print(data_list)                      # Returns none, removing item from list, ValueError is raised if value does not exist ['c', 'd', 'e']

removed = data_list.pop(1)            # Pop method removes the item at given index and returns it.
print(removed)                        # Returns last item on the list if no index, IndexError raised outside of range d
print(data_list)                      # ['c', 'e']
```

### Iterating Lists

The term used for going through list elements, i.e. iteration.

* Iterate a for loop directly
* Using the Python built-in `enumerate()` function
* Using the Python built-in `reversed()` function

**Using a for loop directly**
```py
for i in loop
    print(this)
```
**Using the Python built-in `enumerate()` function**
```py

```
**Using the Python built-in `reversed()` function**
```py

```
Ordered sequences of data. A collection of items.

Lists are a form of arrays. What is the difference?

Container around data w/ pros and cons for accessing that data.

## Packages

The differences between libraries and packages.

Library | Executable
--------|---------------
Created for Reusability | Created for Running Program
Non-Executables | Executable
Importable | Non-Importable
Name Agnostic | Only be Named Main
No Main Function | func main

## Scope

## Dictionaries
