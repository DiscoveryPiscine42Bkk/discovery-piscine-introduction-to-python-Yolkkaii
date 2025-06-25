#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("None")
    sys.exit(0)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

to_print = []

for i in range(num1, num2 + 1):
    to_print.append(i)

print(to_print)
