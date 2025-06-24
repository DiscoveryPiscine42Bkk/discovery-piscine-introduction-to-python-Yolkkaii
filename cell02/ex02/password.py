#variable for the password
password = "SuperSecret123"

#variable to get the user's input
inputPW = str(input("Enter the password: "))

#function to check if the input password matches the correct password
def check_Password(inputPW):
    if inputPW == password:
        print("Access granted.")
    else:
        print("Access denied.")

#run the function with user's input
check_Password(inputPW)

input("\nPress Enter to exit the program")