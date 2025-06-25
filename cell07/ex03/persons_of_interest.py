#!/usr/bin/env python3

def famous_births(famous_people):
    sorted_figures = sorted(famous_people.items(), key=lambda item: item[1]["date_of_birth"])

    for identifier, person_data in sorted_figures:
        name = person_data["name"]
        date_of_birth = person_data["date_of_birth"]
        print(f"{name} is a great scientist born in {date_of_birth}.")

    

if __name__ == "__main__":
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)
