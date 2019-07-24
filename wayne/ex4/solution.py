#!/usr/bin/env python3

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def get_number():
    return int(input("Give me a number "))

def main():
    number = get_number()
    result = filter(lambda x: number % x==0,range(1,number+1))
    print(list(result))

if __name__ == "__main__":
    main()