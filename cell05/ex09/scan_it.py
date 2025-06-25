#!/usr/bin/env python3

import sys
import re

def scan_it():
    if len(sys.argv) != 3:
        print("None")
        sys.exit(1)
    else:
        key_word = sys.argv[1]
        string = sys.argv[2]
        found = len(re.findall(key_word, string))
        print(found)

scan_it()