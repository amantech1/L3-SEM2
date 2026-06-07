# Program to collect details of five books, store them in a dictionary, and display the stored information.

# Empty dictionary to store books
books = {}

# For Loop
for i in range(5):

    print("\nEnter details of Book", i + 1)

    # Accept book details
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    cost = float(input("Cost: "))

    # Store details in dictionary
    books[title] = {
        "Author": author,
        "ISBN": isbn,
        "Cost": cost
    }

# Display all books
print("\nBook Details")

for title, details in books.items():
    print(title, ":", details)