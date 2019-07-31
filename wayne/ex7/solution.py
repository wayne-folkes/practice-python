#!/usr/bin/env python3

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(list(filter(lambda x: x % 2==0,a)))

if __name__ == "__main__":
    main()