# swap two variables without using a third variable

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

# swap the values of a and b
a, b = b, a

print(f"After swapping a = {a} and b = {b}")
print(f"a = {a} and b = {b}")