#variables to get two numbers
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))

#function to multiply two numbers
def multiply(x, y):
    result = x * y
    return result

#print the result
print(f"The result is: {multiply(x, y)}")

input("\nPress Enter to exit the program")