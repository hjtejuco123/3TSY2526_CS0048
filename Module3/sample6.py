def celsius_to_fahrenheit(celsius):
    """This function converts Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

# Get user input
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f:.2f}°F")