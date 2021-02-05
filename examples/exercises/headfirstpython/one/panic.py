#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

# Turn the list into On Tap

phrase = "Don't Panic!"

plist = list(phrase)

print(phrase)
print(plist)

for i in range(4):
    plist.pop()     # pops the last four off

plist.pop(0)        # pops the D at the beginning
plist.remove("'")   # remove the '

# popa = plist.pop()
# popb = plist.pop()

# print(popa)
# print(popb)
# print(plist)

plist.extend([plist.pop(), plist.pop()])

plist.insert(2, plist.pop(3)) # move the space by pop() and insert()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
