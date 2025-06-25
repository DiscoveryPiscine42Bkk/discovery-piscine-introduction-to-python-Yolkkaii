#!/usr/bin/env python3

#variable for a number less than 25
number = int(input("Input a number less then 25: "))

if number >= 25:
    print("Error.")
elif number < 25:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}.")
        number += 1

