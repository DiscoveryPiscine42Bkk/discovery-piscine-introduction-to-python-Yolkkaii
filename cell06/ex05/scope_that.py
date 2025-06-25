#!/usr/bin/env python3

def add_one(param):
    param += 1
    return param

if __name__ == "__main__":
    var = 42
    print(f"Original variable: {var}\nNew variable: {add_one(var)}")
