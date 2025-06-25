#!/usr/bin/env python3

import sys

def count_string():
    if len(sys.argv) != 2 or "z" not in sys.argv[1]:
        print("None")
        sys.exit(1)

    to_find = "z"
    string = sys.argv[1]
    count = string.count(to_find)
    
    print(count)

count_string()