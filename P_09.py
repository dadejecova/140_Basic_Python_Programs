# Solve a quadratic equation

# Standart form of a quadratic equation is ax^2 + bx + c = 0
# a, b, c are coefficients
# x is the variable
# Quadratic formula is x = (-b ± √(b^2 - 4ac)) / 2a

import math
# input the values of a, b and c
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# check if it is positive, negative or zero
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The roots are real and different: x1 = {x1} and x2 = {x2}")
elif d == 0:
    # if the discriminant is zero, the roots are real and repeat
    r = -b / (2*a)
    print(f"The roots are real and repeat: x = {r}")
else:
    # if the discriminant is negative, the roots are complex and different
    real = -b / (2*a)
    imaginary = math.sqrt(abs(d)) / (2*a)
    print(f"The roots are complex and different: x1 = {real} + {imaginary}i and x2 = {real} - {imaginary}i")
    
