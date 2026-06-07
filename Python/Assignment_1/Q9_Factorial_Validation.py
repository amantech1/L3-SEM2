"""Finds the factorial of any number taken as an input from the user
validate the user's input whether it is a number or not and then only perform the operation
n case of other than number as an input, display an error as “Not a number."""

num = input('Enter a number: ')

if num.isdigit():
    num = int(num)

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print('Factorial =', fact)

else:
    print('Not a number.')