# Program to create a function that accepts a list of names and returns them in sorted order.

# Function to sort names alphabetically
def sort_names(names):
    return sorted(names)

# Initializing list of names
names_list = ["Ram", "Hari", "Sita", "Gita"]
print("Given Names:", names_list)

# Function call
sorted_names = sort_names(names_list)

# Display Results
print("Sorted Names by Alphabet:", sorted_names)