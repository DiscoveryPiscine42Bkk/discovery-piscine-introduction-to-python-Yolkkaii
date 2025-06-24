#!/usr/bin/env python3

#variable to recieve a number from the user
x = int(input("Input a number : "))

#function to check if number is equal to zero or not
def check_Number(x):
    if x == 0 :
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")

check_Number(x)