#!/usr/bin/env python3

def array_of_names(name_dict):
    full_namelist = []
    for first_name, last_name in name_dict.items():
        upper_first = first_name.capitalize()
        upper_last = last_name.capitalize()

        full_name = f"{upper_first} {upper_last}"

        full_namelist.append(full_name)

    return full_namelist

if __name__ == "__main__":

    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }

    print(array_of_names(persons))