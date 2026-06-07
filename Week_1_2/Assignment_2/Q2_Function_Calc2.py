# Program to create separate functions for addition, subtraction, multiplication, division, modulo division, and floor division.

# Functions for addition, substraction, multiplication, division, modulo and floor division
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modulo(a, b):
    return a % b

def floor_div(a, b):
    return a // b

# Accept input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display Results
print("1. Addition =", add(a, b))
print("2. Subtraction =", sub(a, b))
print("3. Multiplication =", mul(a, b))
print("4. Division =", div(a, b))
print("5. Modulo Division =", modulo(a, b))
print("6. Floor Division =", floor_div(a, b))