# Program to create a function that calculates and returns the factorial of a given number.

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Accept input from user
num = int(input("Enter a number: "))

# Display Results with function call
print("Factorial of", num, "=", factorial(num))