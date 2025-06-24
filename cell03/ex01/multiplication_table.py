#variable to get the number
number = int(input("Input a number: "))

#function to print the multiplication table
def multiplication_table(number):
    multNum = 0
    while multNum <= 9:
        print(f"{number} x {multNum} = {number * multNum}")
        multNum += 1

#call the function
multiplication_table(number)

input("\nPress Enter to exit the program")