#!/usr/bin/env python3

import sys

def get_first_param():
    if len(sys.argv) < 2:
        print("None")
        sys.exit(1)
    else:
        print(sys.argv[1])
        
get_first_param()