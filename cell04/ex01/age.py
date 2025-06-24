#!/usr/bin/env python3

num = 10
age = int(input("What's your age: "))

print(f"You are {age} years old.")

for i in range(0, 3):
    print(f"In {num} years, you'll be {age + num}")
    num += 10