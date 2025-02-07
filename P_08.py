# Display a calendar

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)

print(f"Here is the calendar for {month}/{year}")
print(cal)