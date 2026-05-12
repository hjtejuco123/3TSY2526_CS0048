def calculate_interest(principal, rate=0.05, years=1):
    """Calculate simple interest with default rate and time"""
    interest = principal * rate * years
    return principal + interest

# Get user input
principal = float(input("Enter principal amount: $"))
use_defaults = input("Use default rate (5%) and time (1 year)? (yes/no): ").lower()

if use_defaults == "yes":
    total = calculate_interest(principal)
else:
    rate = float(input("Enter interest rate (as decimal): "))
    years = int(input("Enter number of years: "))
    total = calculate_interest(principal, rate, years)

print(f"Total amount after interest: ${total:.2f}")