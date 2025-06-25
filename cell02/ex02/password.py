#!/usr/bin/env python3

#variable for the password
password = "SuperSecret123"

#variable to get the user's input
inputPW = str(input("Enter the password: "))

if inputPW == password:
    print("Access granted.")
else:
    print("Access denied.")
