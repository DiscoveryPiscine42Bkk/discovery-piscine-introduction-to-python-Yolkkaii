#!/usr/bin/env python3

#variables to get two numbers
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))

result = x * y
print(f"{x} x {y} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
