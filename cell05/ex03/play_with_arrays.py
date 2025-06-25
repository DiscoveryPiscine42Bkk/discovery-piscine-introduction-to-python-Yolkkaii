#!/usr/bin/env python3

org_array = [2, 8, 9, 48, 8, 22, -12, 2]
#use a set to avoid any duplicate numbers
new_array = set()

for i in org_array:
    if i > 5:
        i += 2
        new_array.add(i)

print(f"Original array: {org_array}\nNew array: {new_array}")