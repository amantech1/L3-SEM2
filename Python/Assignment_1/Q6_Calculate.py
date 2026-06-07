#Input the number of 5 subjects from the user, calculate the average, total, percentage and division of the students

a = float(input("Enter marks in Maths: "))
b = float(input("Enter marks in Physics: "))
c = float(input("Enter marks in Computer: "))
d = float(input("Enter marks in English: "))
e = float(input("Enter marks in Chemistry: "))

sum = a+b+c+d+e
average = sum/5
percent = (sum/500)*100

print('\nThe total marks is: ', sum)
print('The average marks is: ', average)
print('The percentage is: ', percent, '\n')

if percent >= 80:
    print('The user obtained Distinction')
elif percent >= 60:
    print('The user obtained First Division')
elif percent >= 50:
    print('The User obtained Second Division')
elif percent >= 45:
    print('The user obtained Third Division')
elif percent < 45:
    print('The User Failed')
else:
    print('Wrong Data')