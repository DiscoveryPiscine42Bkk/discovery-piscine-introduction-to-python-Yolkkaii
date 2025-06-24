#!/usr/bin/env python3

num = float(input("Give me a number: "))

def is_float(num):
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a float.")
    

is_float(num)