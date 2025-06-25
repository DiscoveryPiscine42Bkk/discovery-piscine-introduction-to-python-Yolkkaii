#!/usr/bin/env python3

import sys

def match_param():
    #check if the number of parameters is equal to 1 (not counting the script name)
    if len(sys.argv) != 2:
        print("None")
        #to exit from the program with out an error
        sys.exit(1)
    
    #parameter is at index 1 (scirpt name is at index 0)
    parameter = sys.argv[1]

    word = input("What was the parameter?\n")

    #check to see if the word matches the parameter
    if word == parameter:
        print("Good job!")
    else:
        print("Nope, sorry.")

match_param()