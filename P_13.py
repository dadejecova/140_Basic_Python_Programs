# Check leap year

year = int(input("Enter a year: "))

# Divided by 100 means century
# Century divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")

# not divided by 100 means not a century
# year divided by 4 is leap year

elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")

# if not divided by both 400 and 4 is not a leap year

else:
    print(f"{year} is not a leap year.")