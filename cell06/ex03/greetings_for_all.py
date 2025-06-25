#!/usr/bin/env python3

def greetings(name = ""):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    elif len(name) < 1:
        print(f"Hello, noble stranger.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
