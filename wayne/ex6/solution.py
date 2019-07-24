#!/usr/bin/env python3

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)



def main():
    my_string = input("Give me a string ")
    if my_string == my_string[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a plaindrome :(")

if __name__ == "__main__":
    main()