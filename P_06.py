# Convert Kilometers to miles

# 1 Kilometer = 0.621371 miles
# 1 mile = 1.60934 Kilometers
# 1 Kilometer = 1000 meters
# 1 meter = 0.001 Kilometers

kilometers = float(input("Enter the distance in Kilometers: "))

c_factor = 0.621371
miles = kilometers * c_factor

print(f"{kilometers} Kilometers is equal to {miles} miles")