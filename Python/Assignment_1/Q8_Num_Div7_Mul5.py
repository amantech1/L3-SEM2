#Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5
#By given numbers between 2000 and 3200 (both included)

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num)

#By taking input from user
start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        print(num,)