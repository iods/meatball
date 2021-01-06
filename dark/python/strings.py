# Dark Society Python Development
#
# The Basics
# Data Types: Strings
intro = 'An introduction to Data Types: Strings.'
print(intro)

 # String variables
string = 'Speak Softly and Hustle Hard.'
string_long = '''
Never let the odds keep you from doing what you know in your
heart you were meant to do. Join me, and together we can rule
the galaxy. What are the odds?
'''
string_three = 'OneTwoThreeFour'
string_four = '1234'
string_dec = '10.5'
string_id = 'this_is_id'


# Basic Functions
print(type(string))                   # Returns the data type of the string. (str)
print(len(string))                    # Returns the length of a string.
print(len(string_long))
print('  Speak Softly  '.strip())     # Strips the whitespace from both ends of a string.
print('Hustle Hard'.strip('H'))       # Strips the the letters from both ends in a string. (a would not work)
print(string.split())
print('Help Me'.replace('Me', 'You')) # Replaces first parameter w/ second parameter.
print('Help You'.startswith('Help'))  # Returns true/false if the string begins w/ parameter.
print('Help Me'.endswith('You'))      # Returns true/flase if the string ends w/ parameter.
print('red bull'.upper())             # Returns the string in all uppercase characters.
print('GIVES YOU WINGS'.lower())      # Returns the string in all lowercase characters.
print('stRINgs'.swapcase())           # Returns the string with the character case swapped.
print(string.capitalize())            # Returns the first character of the string capitalized.
print(string_long.count('odds'))      # Returns an int of the count for number of times the character or phrase exists.
print(string_long.find('odds'))       # Returns the index of the first instance of a character or phrase.
print(string_long.find('oddity'))     # Returns -1 if the index does not exist.
print(string.isalnum())               # Checks if is alphanumeric character - False - spaces
print(string_long.isalnum())          # False
print(string_three.isalnum())         # True
print(string_three.isalpha())         # True - No spaces
print(string_four.isalpha())          # False ( not characters of the alphabet )
print(string_four.isdigit())          # Checks if it is integer or not and returns true/false
print(string_dec.isdecimal())         # False, it is a float
print(string_id.isidentifier())       # True, starts with a letter not number?


# String Indexes
# Python stores strings as sequences of letters in memory
string_index = 'String Indexes'

print(string_index[0])      # First letter
print(string_index[3])      # i (third index of the string)
print(string_index[0:4])    # Stri - Starts at the 0 index and goes to the fourth
print(string_index[4:14])   # ng Indexes - Starts at the fourth index and goes to the 14th
print(string_index[:])      # String Indexes
print(string_index[1:])     # tring Indexes
print(string_index[:1])     # S
print(string_index[-1])     # s (- starts from the back and reverse)
print(string_index[-5])     # d
print(string_index[::1])    # String Indexes
print(string_index[::-1])   # sexednI gnirtS
print(string_index[0:10:2]) # [start:end:step] slicing - Srn n


# String Concatenation and Formatted Strings
greet = 'Hey, there'
name = 'Tiffany'

print(greet + name + '. xD.')            # Outputs two concatenated strings with no space.
print(greet + ', ' + name + '. xD.')     # Outputs can get dirty w/ larget amount of vars.
print('{}, {}. xD.'.format(greet, name)) # Fromatted strings
print(f'{greet}, {name}. xD.')           # 3.6 and newer allows f-strings
print(f'{greet}, {name.upper()}. xD.')   # Apply basic functions to the formatted strings


end = intro.replace('introduction', 'ending')
print(end)
