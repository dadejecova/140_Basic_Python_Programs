# Check if a number is positive, negative or zero.

n = int(input("Enter a number: "))
if n > 0:
    print(f"{n} is a positive number.")
elif n < 0:
    print(f"{n} is a negative number.")
else:
    print(f"{n} is zero.")