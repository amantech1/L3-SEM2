#Solving the expressions in a python program

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

x = a**2 + 2*a*b + b**2
y = a**5 + 2*a*b*c + b**3 + c**4
z = a**7 + 5*(a**3)*(b**2)*(c**6) + b**7

print('\na² + 2ab + b²: ', x)
print('a⁵ + 2abc + b³ + c⁴: ', y)
print('a⁷ + 5a³b²c⁶ + b⁷: ', z)
