#string default parameters
def format_address(street, city, country="USA"):
    """Format an address with default country"""
    return f"{street}\n{city}, {country}"

# Get user input
street = input("Enter street address: ")
city = input("Enter city: ")
use_default_country = input("Is the country USA? (yes/no): ").lower()

if use_default_country == "yes":
    address = format_address(street, city)
else:
    country = input("Enter country: ")
    address = format_address(street, city, country)

print("\nFormatted address:")
print(address)