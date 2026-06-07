#Display the prime number between 2 numbers input by the users. Also print the sum of all the prime numbers

first = int(input('Enter first number: '))
last = int(input('Enter second number: '))
sum = 0

print('Prime numbers are:\n')

for num in range(first, last + 1):
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)
            sum += num

print('Sum of prime numbers = ', sum)