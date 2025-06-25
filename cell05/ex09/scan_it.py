#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("None")
    sys.exit(0)
else:
    key_word = sys.argv[1]
    string = sys.argv[2]
    found = len(re.findall(key_word, string))
    print(found)
