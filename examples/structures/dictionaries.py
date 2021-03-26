#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Introduction to Data Types: Dictionaries

Out of the box, dictionaries allow the storage and manipulation
of any collection of key/value pairs. Probably the most powerful
data type in Python. Like lists are mutable, unlike lists are not
sequenced. They are not necessarily a sequence of numbered objects
but more a key value store.
"""


def list_example():
    """List Example

    Describes the difference between a list and dictionary by creating
    a list, and accessing it's objects through indexes, not possible in a
    python Dictionary data type.
    """
    firstname = 'Rye'
    lastname = 'Miller'
    age = '43'
    city = 'Boston'

    developer = [firstname, lastname, age, city]
    print('Details:', str(developer))

    print('Last Name: ', str(developer[1]))  # Accessible through it's index
    print('City: ', str(developer[3]) + '\n')       # Objects are called by their indexes in lists


def dictionary_example():
    """Dictionary Example

    Takes the same values as above, but uses them as a dictionary and
    shows how to access the objects through their keys, not the indexes.
    """
    developer = {
        'firstname': 'Tanner', 'lastname': 'Miller', 'age': '19', 'city': 'tallahassee'}  # curly brackets, not []

    print('Details: ', str(developer))
    # print('Last Name: ', str(developer[1]))         # will throw an error
    print('Last Name: ', str(developer['lastname']))  # accessed through the key, not index
    print('City: ', str(developer['city']) + '\n')    # fetch objects by searching keys

    manager = {}
    manager['firstname'] = 'Robert'
    manager['lastname'] = 'Redford'
    manager['age'] = '74'
    manager['city'] = 'Los Angeles'

    print('Details: ', str(manager) + '\n')


def dictionary_construction():
    """Dictionary Construction

    Basic creation of dictionaries through various usages.
    """
    developer = dict(firstname='Rye', lastname='Miller', age='45', city='Palm Springs')
    print('Details: ', developer, '\n')

    designer = dict(zip(
        ['firstname', 'lastname', 'age', 'city'], ['Donald', 'Sutherland', '88', 'Brooklyn']))
    print('Details: ', designer, '\n')

    senior_developer = {'1001': {
        'fullname': {
            'firstname': 'Jon', 'lastname': 'Denver'},
        'contact': {
            'home': 5553021331, 'mobile': 5553023113},
        'age': 43,
        'address': ['Aspen']}
    }
    print('Details: ', senior_developer, '\n')

    senior_developer['1001']['subject'] = ['PHP', 'Go', 'Python', 'JavaScript']  # add a list of subjects
    print('Details: ', senior_developer, '\n')
    print('Senior Developer (name): ',
          senior_developer['1001']['fullname']['lastname'], ', ', senior_developer['1001']['fullname']['firstname'])

    print('Address: ', senior_developer['1001']['address'][0] + '\n')

    senior_developer['1001']['address'].append('Colorado')
    print('Address: ', senior_developer['1001']['address'][0], ', ', senior_developer['1001']['address'][1] + '\n')


def dictionary_deconstruction():
    """Dictionary Deconstruction

    Basic removal of a dictionary.
    """

    developer = {
        'firstname': 'Tanner', 'lastname': 'Miller', 'age': '19', 'city': 'tallahassee'}

    del developer
    # print(developer) throws an error about reference before assignment (deleted)


if __name__ == "__main__":
    print('\n')
    list_example()
    dictionary_example()
    dictionary_construction()
    dictionary_deconstruction()

