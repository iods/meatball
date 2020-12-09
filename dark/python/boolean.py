# Dark Society Python Development
#
# The Basics
# Data Types: Boolean

bool(True)
bool(False)

print('Is True:', True)
print('Is False:', False)
print('Is False:', bool(-0))
print('Is False:', bool(0))
print('Is True:', bool(1))
print('Is True:', bool(0.5))
print('Is True:', bool('0'))
print('Is True:', bool('True'))
print('Is True:', bool('False'))
print('Is False:', bool(False))
print('Is True:', bool('A Random String'))

# All values are considered "truthy" except for the following, which are "falsy":
#     None
#     False
#     0
#     0.0
#     0j
#     Decimal(0)
#     Fraction(0, 1)
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     '' - an empty str
#     b'' - an empty bytes
#     set() - an empty set
#     an empty range, like range(0)
#     objects for which
#         obj.__bool__() returns False
#         obj.__len__() returns 0

# all of the below evaluate to False. Everything else will evaluate to True in Python.

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))
