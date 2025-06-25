#!/usr/bin/env python3

import sys

count = 0

for i in range(1, len(sys.argv)):
    count += 1

print(f"Number of parameters: {count}")
