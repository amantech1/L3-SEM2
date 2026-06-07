"""To Find the sum of odd and even numbers input from the user.
The program takes an input continuously until the user wants to exit the program.
The program is menu driven where the user should be asked whether they want to continue with the program or not."""

#initializing
sum_even = 0
sum_odd = 0

choice = 'yes'

while choice.lower() == 'yes':
    num = int(input('Enter a number: '))

    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

    choice = input('Do you want to continue? (yes/no): ')

#Printing the Result
print('Sum of Even Numbers =', sum_even)
print('Sum of Odd Numbers =', sum_odd)