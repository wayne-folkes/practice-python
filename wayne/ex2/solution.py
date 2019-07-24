#!/usr/bin/env python3

# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

def get_number():
    return int(input("Give me number "))

def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False

def main():
    number = get_number()
    if is_even(number):
        print("This number is even")
    else:
        print("This nubmer is odd")

if __name__ == "__main__":
    main()