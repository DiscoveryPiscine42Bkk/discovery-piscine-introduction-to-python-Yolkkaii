#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("None")
    sys.exit(0)

print(f"parameters: {len(sys.argv) - 1}")

for i in range(1, len(sys.argv)):
    param = sys.argv[i]
    print(f"{param}: {len(param)}")
