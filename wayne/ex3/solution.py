#!/usr/bin/env python3

# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, 
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from
#  the original list a that are smaller than that number given by the user.

ceiling = 5

def get_number():
    return int(input("Give me a number "))

def is_less_than(x):
    return ceiling > x

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(list(filter(is_less_than,a)))
    global ceiling
    ceiling=get_number()
    print(list(filter(is_less_than,a)))

if __name__ == "__main__":
    main()