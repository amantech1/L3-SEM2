# Program to continuously accept numbers from the user and separate them into even and odd number lists.

# Lists to store even and odd numbers
even = []
odd = []

# Loop until user wants to stop
while True:

    # Accept number from user
    num = int(input("Enter a number: "))

    # Check even or odd
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    # Ask user whether to continue
    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() == 'n':
        break

# Display results
print("Even Numbers:", even)
print("Odd Numbers:", odd)