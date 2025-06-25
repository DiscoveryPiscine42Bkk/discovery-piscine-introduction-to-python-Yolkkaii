#!/usr/bin/env python3

org_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in org_array:
    if i > 5:
        i += 2
        new_array.append(i)

print(f"Original array: {org_array}\nNew array: {new_array}")
