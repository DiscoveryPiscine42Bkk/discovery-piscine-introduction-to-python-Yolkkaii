#!/usr/bin/env python3

import sys

def shrink(text = ""):
    return text[slice(0, 8)]

def enlarge(text = ""):
    while len(text) < 8:
        text += "Z"
    return text

if len(sys.argv) < 2:
    print("None")
    sys.exit(0)
else:
    for i in range(1, len(sys.argv)):
        current_arg = sys.argv[i]

        if len(current_arg) < 8:
            modified_arg = enlarge(current_arg)
            print(modified_arg)

        elif len(current_arg) > 8:
            modified_arg = shrink(current_arg)
            print(modified_arg)
            
        else:
            print(current_arg)
