# Convert Celsius to Fahrenheit

# 1 Celsius = 33.8 Fahrenheit
# 1 Fahrenheit = -17.2222 Celsius
# 1 Celsius = 100 Kelvin
# 1 Kelvin = -272.15 Celsius

celsius = float(input("Enter the temperature in Celsius: "))

# celsius to fahrenheit
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")