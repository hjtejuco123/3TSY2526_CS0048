# Calculate discount based on purchase amount Example 10: Discount calculation
amount = 1000
if amount >= 1000:
    discount = amount * 0.1  # 10% discount
else:
    discount = amount * 0.05  # 5% discount
total = amount - discount
print(f"Original: ${amount}, Discount: ${discount:.2f}, Total: ${total:.2f}")