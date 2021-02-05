#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

# Check if Magician and an Expert, tell them "You are a Master Magician!"
# Check if Magician but not Expert, tell them "Hey, you are getting there."
# Check if not a Magician, tell them "I think you need magic powers?"

is_magician = True
is_expert = False

if is_expert and is_magician:
    print("You are a master Magician!")

elif is_magician and not is_expert:
    print("Hey, you are getting there.")

elif is_magician is False:
    print("I think you need magic powers.")
