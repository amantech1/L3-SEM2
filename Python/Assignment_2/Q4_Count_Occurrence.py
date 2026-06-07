# Program to create a function that accepts a list of numbers and displays the occurrence of each number.

# Function to count occurrences
def occur(numbers):
    for num in set(numbers):

        # Display Results
        print(num, "occurs", numbers.count(num), "times")

# Initializing list of numbers
num_list = [1, 2, 3, 4, 3, 2, 1, 2, 2, 1]

print('List of Numbers:', num_list, '\n')

# Function Call
occur(num_list)