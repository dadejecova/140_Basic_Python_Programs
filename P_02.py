# Write a program to do arithmetical operations addition and division.

# Adittion

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print(f"Sum of {num1} and {num2} is: {result}")

if num2 == 0:
    print("Division by zero is not possible")
else:
    result = num1 / num2
    print(f" Division of {num1} and {num2} is: {result}")
