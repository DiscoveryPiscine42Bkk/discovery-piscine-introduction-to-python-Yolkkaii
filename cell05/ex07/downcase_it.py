#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("None")
    sys.exit(0)
else:
    print(sys.argv[1].lower())
