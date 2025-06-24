#variable for a number less than 25
number = int(input("Input a number less then 25: "))

#function to check the number
def check_number(number):
    if number >= 25:
        print("Error.")
    elif number < 25:
        while number <= 25:
            print(f"Inside the loop, my variable is {number}.")
            number += 1

#call the function
check_number(number)

input("\nPress Enter to exit the program")