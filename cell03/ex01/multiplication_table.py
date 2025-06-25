#!/usr/bin/env python3

#variable to get the number
number = int(input("Input a number: "))

multNum = 0

while multNum <= 9:
    print(f"{number} x {multNum} = {number * multNum}")
    multNum += 1
