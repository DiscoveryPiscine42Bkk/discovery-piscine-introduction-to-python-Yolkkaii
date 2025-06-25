#!/usr/bin/env python3

import sys

def reverse_params():
    if len(sys.argv) < 3:
        print("None")
        sys.exit(1)
    else:
        for i in range(len(sys.argv) - 1, 0, -1):
            to_print = sys.argv[i]
            print(to_print)

reverse_params()