#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("None")
    sys.exit(0)
else:
    string_to_check = sys.argv[1]

    if "z" not in string_to_check:
        print("None")
        sys.exit(0)
    else:
        to_find = "z"
        count = string_to_check.count(to_find)
        print(count)
