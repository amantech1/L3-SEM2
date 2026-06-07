# Program to accept a list of numbers and return a new list after removing duplicate values.

# Input numbers from user
numbers = list(map(int, input("Enter numbers: ").split()))

# Removing duplicates using "set"
unique_nums = list(set(numbers))

# Display Results
print("List of numbers without duplicates:", unique_nums)