#!/usr/bin/env python3

import datetime
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

TARGET_AGE = 100

def get_name():
    return input("What is your name? ")

def get_age():
    return int(input("What is your age? "))

def get_year_till_age(current_age,target_age):
    current_year = datetime.datetime.now().year
    age_diff = target_age - current_age
    target_year = current_year + age_diff
    return target_year

def get_another_number():
    return int(input("Give me another number "))

def print_message(times=1, **kwargs):
    for _ in range(times):
        print("%s you will turn %s in the year %s" %(kwargs['name'], TARGET_AGE, kwargs['target_year']))

def main():
    name = get_name()
    age = int(get_age())
    target_year = get_year_till_age(age,TARGET_AGE)
    args={"name":name,"target_year":target_year}
    print_message(**args)
    more_times = get_another_number()
    print_message(more_times,**args)

if __name__ == "__main__":
    main()