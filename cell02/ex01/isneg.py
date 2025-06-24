#!/usr/bin/env python3

#get the user's input
x = int(input("Input a number: "))

#function to check if number is positive, negative or zero
def check_Number(x):
    if x < 0:
        print("This number is negative number.")
    elif x > 0:
        print("This number is positive number.")
    elif x == 0:
        print("This number is both a positive and a negetive number.")

#run the function with the user's input (x) as the argument
check_Number(x)

