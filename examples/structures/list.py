#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Introduction to Data Types: Lists

Lists are built in data structures in Python. It is a represented
collection of data points contained in square brackets. Lists are
mutable, which is why they are used frequently; however, mutability
must take some care and some concern.
 1. Allows duplication
 2. Mutability allows alteration after creation
 3. Items in a list need not be the same type
 4. Contain any type or a mix of data types
"""

global characters, family, languages, letters, numbers, strains, types

# Don't forget, lists are mutable, ordered, have indexing/slicing, and duplicate members.
# Another thing, mutability means once we define a list, individual items in
# that list can be updated later.


def list_construction():
    """Assignment Operator & Copying of Lists

    We construct lists by listing the items, using the list()
    function, and working with existing lists.
    """
    print("constructing a list")
    global characters, family, languages, letters, numbers, strains, types

    data_list = list()
    print(type(data_list))

    data_list = []
    print(len(data_list))

    # lists store an ordered collection of data/items of diff types
    characters = [
        'Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Severus Snape', 'Jack Skellington',
        'Darth Vader', 'Luke Skywalker', 'John Denver', 'Eddie Murphy']

    family = [
        'Steve Milbury', 'Alison Wonderland', 'Tanner Cabrera', 'Tiffany Camillle', 'Patty Suarez',
        'Jim Jeffery', 'Riley Otto', 'Nick Otto', 'Bill Burr', 'Edward Jones']

    company = family[1:4]                   # create a list from a slice
    print('Company:', company)
    print('Company Length:', len(company))

    technology = "docker"                   # create a list from a string
    print(list(technology))

    languages = [
        'PHP', 'JavaScript', 'Go', 'Python', 'Bash', 'SQL', 'Java', 'Rust']

    letters = ['a', 'b', 'c', 'd', 'e', 'd', 'c', 'b', 'a']

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    number = list(range(10))                # create a list from a range of numbers
    print(number)

    strains = [
        'Blue Dream', 'OG Kush', 'Durban Poison', 'Headband', 'Purple Rain', 'Grandmas Cookies',
        'Jellybean Peanut', 'Sour Diesel', 'Grand Daddy Purple']

    types = ['text', 12345, True, {'name': 'Steve', 'strain': 'Headband'}]

    print(characters + family)      # list concatenation links/chains lists together easily
    print([*languages, *letters])   # splat operator will unpack complex data types
    print([*numbers, [6], *types])  # list comprehension helps splatting and control


def list_access():
    """Accessing Lists

    Access individual and multiple items in a list using
    indexing, slicing, and range; among other things.
    """
    print("accessing a list")

    print('Characters:', characters)
    print('Family:', family)
    print('Languages:', languages)
    print('Numbers:', numbers)
    print('Strains:', strains)
    print('Types:', types)

    print('Character:', characters[1])       # Access through positive indexing
    print('Family Member:', family[4])       # each item has an assigned value, starting w/ 0
    print('Language:', languages[3])         # since python is 0 indexed language
    print('Number:', numbers[0])
    print('Strain:', strains[5])
    print('Type:', types[2])

    print('Character (-):', characters[-1])  # Access through negative indexing
    print('Member (-):', family[-4])         # negative indexing starts at the end, not 0
    print('Language (-):', languages[-3])    # this is useful when not knowing length of list
    print('Number (-):', numbers[-5])
    print('Strain (-):', strains[-2])
    print('Type (-3):', types[-2])

    print(numbers.index(4))                  # index() method returns first index where that value occurs
    print(numbers.index(4, 8))               # index() method also allows to specify index where to start search
    print(numbers.count(4))                  # count() method counts how many times it occurs in the list


def list_conditional():
    """Conditionals

    Check whether or not the list has a particular item within it,
    it's emptiness, and it's relationship with other lists.
    """
    print("m.c conditioning a list")

    if len(types) > 0:
        print("First way of checking if it is not empty.")

    if types:
        print('Second way of checking if it is not empty.')

    if types != []:
        print('Third way of checking if it is not empty.')

    names = list(family)
    names.remove('Riley Otto')

    # set(family).issubset(set(names))
    # set(names).issubset(set(family))


def list_modification():
    """Manipulating Lists

    Appending, inserting, removing elements across lists. Change
    the order of lists with methods.
    """
    print("modifying a list")

    strains.append('Lemon Haze')           # append() method will add a member to the end of a list (done in place)
    print(strains)

    strains.extend(languages)              # extent() method acts much like append but for whole lists
    print(strains)
    print(family + characters)             # extend() method alternatively allows to use + to add two lists together

    strains.sort()                         # sort() method will sort and alter the original list
    print(strains)
    strains.sort(reverse=True)             # sort() method allows to specify order (low to high, high to low)
    print(strains)

    strains.remove('Jellybean Peanut')     # remove() method, removes the member from the list
    print(strains)

    print(strains.pop(0))                  # pop() method removes an item from the index, returning it
    print(strains.pop())                   # pop() method will return the last member if no index is provided

    strains.insert(1, 'Jellybean Peanut')  # insert() method inserts a member before the specified index
    print(strains)


def list_iteration():
    """Iterating Lists

    Iterate lists using themselves and in combination with
    the enumerate() and reversed() functions.
    """
    print("iterating a list")

    names = zip(characters, family)                  # zip() returns an iterator of tuples
    for name in names:                               # combining elements of a list at their index
        print(name)

    names = family
    for name in range(len(names)):                   # using a simple loop to iterate them works too
        print(names[name])

    for count, member in enumerate(family, 1):
        print(f'Family Member #{count} - {member}')  # using enumerate()

    for member in reversed(family):                  # reversed() function to iterate through in reverse
        print(member)


def list_destruction():
    """Destruction?

    Removal and deletion of items within a list. Not quite full
    list destruction, yet.
    """
    print("destroying items in a list")

    del(languages[0])               # del() method will delete an item from a list
    print(languages)                # del() method. taking the index as the item to be removed

    languages.remove('JavaScript')  # remove() method passes the item value to be removed, not index
    print(languages)

    alpha = numbers.pop()           # pop() method removes an item from the index, last member with no index provided
    print(f'a is {numbers}')
    print(f'b is {alpha}')

    languages.clear()               # clear() method clears the entire list, destruction from construction
    print(languages)


if __name__ == "__main__":
    list_construction()
    list_access()
    list_conditional()
    list_modification()
    list_iteration()
    list_destruction()
