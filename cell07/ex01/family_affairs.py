#!/usr/bin/env python3

def find_the_redheads(members):
    is_redhead = lambda item: item[1] == "red"

    filtered_items = list(filter(is_redhead, members.items()))

    redheads_names = [name for name, _ in filtered_items]

    return redheads_names

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))