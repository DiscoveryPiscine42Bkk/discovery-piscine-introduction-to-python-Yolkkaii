#!/usr/bin/env python3
x = 0

#while loop to print the multiplication table
while x <= 10:
    text = str(f"Table de {x}: ")
    y = 0

    while y <= 10:
       text += str(f"{x * y} ")
       y += 1
    if y > 10:
        x += 1
    print(text)