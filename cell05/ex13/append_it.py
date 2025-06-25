#!/usr/bin/env python3

import sys

def append_it():
    if len(sys.argv) <2:
        print("None")
        sys.exit(1)
    
    for i in range(1, len(sys.argv)):
        if "ism" in sys.argv[i]:
            #use "continue" to skip this iteration
            continue
        else:
            sys.argv[i] += "ism"
            print(sys.argv[i])
            
append_it()