# Program to create a function that accepts two numbers and displays their sum, difference, product, and remainder.

# Function to perform calculations
def calc(a, b):
    print("Sum =", a + b)
    print("Difference =", a - b)
    print("Product =", a * b)
    print("Remainder =", a % b)

# Accept input from user
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

#Function Call
calc(num1, num2)