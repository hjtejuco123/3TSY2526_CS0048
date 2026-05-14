### 1. Square a Number
```python
num = float(input("Enter a number to square: "))
square = lambda x: x ** 2
print(f"Result: {square(num)}")
```

### 2. Check Even/Odd
```python
num = int(input("Enter an integer: "))
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"Number is {is_even(num)}")
```

### 3. Celsius to Fahrenheit
```python
celsius = float(input("Enter temperature in °C: "))
to_fahrenheit = lambda c: (c * 9/5) + 32
print(f"{celsius}°C = {to_fahrenheit(celsius):.1f}°F")
```

### 4. String Length Checker
```python
text = input("Enter text: ")
check_length = lambda s: "Long" if len(s) > 10 else "Short"
print(f"Text is {check_length(text)}")
```

### 5. Positive/Negative Check
```python
num = float(input("Enter a number: "))
sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(f"Number is {sign(num)}")
```

### 6. Palindrome Checker
```python
text = input("Enter a word: ").lower()
is_palindrome = lambda s: s == s[::-1]
print("Palindrome!" if is_palindrome(text) else "Not a palindrome")
```

### 7. Area of Circle
```python
radius = float(input("Enter circle radius: "))
area = lambda r: 3.14159 * r ** 2
print(f"Area = {area(radius):.2f} sq units")
```

### 8. Uppercase Converter
```python
text = input("Enter text: ")
to_upper = lambda s: s.upper()
print(f"Uppercase: {to_upper(text)}")
```

### 9. Leap Year Checker
```python
year = int(input("Enter year: "))
is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print("Leap year!" if is_leap(year) else "Not a leap year")
```

### 10. Miles to Kilometers
```python
miles = float(input("Enter miles: "))
to_km = lambda m: m * 1.60934
print(f"{miles} miles = {to_km(miles):.2f} km")
```

### 11. Simple Age Classifier
```python
age = int(input("Enter age: "))
classify = lambda a: "Child" if a < 13 else "Teen" if a < 20 else "Adult"
print(f"Classification: {classify(age)}")
```

### 12. Vowel Checker
```python
char = input("Enter a character: ").lower()
is_vowel = lambda c: c in 'aeiou'
print("Vowel!" if is_vowel(char) else "Not a vowel")
```

### 13. Absolute Value
```python
num = float(input("Enter a number: "))
abs_val = lambda x: x if x >= 0 else -x
print(f"Absolute value: {abs_val(num)}")
```

### 14. List Square Generator
```python
nums = list(map(float, input("Enter numbers (space-separated): ").split()))
squares = list(map(lambda x: x**2, nums))
print(f"Squares: {squares}")
```

### 15. Discount Calculator
```python
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
calc = lambda p, d: p * (1 - d/100)
print(f"Discounted price: ${calc(price, discount):.2f}")
```

### 16. String Reverser
```python
text = input("Enter text to reverse: ")
reverse = lambda s: s[::-1]
print(f"Reversed: {reverse(text)}")
```

### 17. Grade Evaluator
```python
score = float(input("Enter score (0-100): "))
grade = lambda s: 'A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' if s >= 60 else 'F'
print(f"Grade: {grade(score)}")
```

### 18. Prime Number Check
```python
num = int(input("Enter integer to check prime: "))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
print("Prime!" if is_prime(num) else "Not prime")
```

### 19. Binary to Decimal
```python
binary = input("Enter binary number: ")
to_decimal = lambda b: int(b, 2)
print(f"Decimal: {to_decimal(binary)}")  # Handles invalid input via exception
```

### 20. Currency Converter (USD to EUR)
```python
usd = float(input("Enter USD amount: "))
convert = lambda amount: amount * 0.93  # Fixed rate for example
print(f"≈ {convert(usd):.2f} EUR")
```


### 1. Square Even Numbers
```python
nums = list(map(int, input("Enter integers (space-separated): ").split()))
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(f"Squares of even numbers: {result}")
```

### 2. Filter Positive Temperatures
```python
temps = list(map(float, input("Enter temperatures (°C): ").split()))
positive = list(filter(lambda t: t > 0, temps))
print(f"Positive temps: {positive}")
```

### 3. Convert Valid Email Domains
```python
emails = input("Enter emails (comma-separated): ").split(',')
valid_domains = list(map(
    lambda e: e.strip().split('@')[1].lower(), 
    filter(lambda e: '@' in e and '.' in e.split('@')[1], emails)
))
print(f"Valid domains: {valid_domains}")
```

### 4. Filter Prime Numbers
```python
nums = list(map(int, input("Enter integers: ").split()))
primes = list(filter(
    lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)), 
    nums
))
print(f"Prime numbers: {primes}")
```

### 5. Convert Valid Phone Numbers
```python
phones = input("Enter phone numbers (xxx-xxx-xxxx): ").split()
valid = list(map(
    lambda p: p.replace('-', ''), 
    filter(lambda p: len(p) == 12 and p[3] == p[7] == '-', phones)
))
print(f"Formatted numbers: {valid}")
```

### 6. Filter Palindrome Words
```python
words = input("Enter words: ").split()
palindromes = list(filter(
    lambda w: w.lower() == w.lower()[::-1], 
    words
))
print(f"Palindromes: {palindromes}")
```

### 7. Calculate Discounted Prices
```python
prices = list(map(float, input("Enter prices: ").split()))
discount = float(input("Discount %: "))
discounted = list(map(
    lambda p: round(p * (1 - discount/100), 2), 
    filter(lambda p: p > 0, prices)
))
print(f"Discounted prices: {discounted}")
```

### 8. Filter Valid ZIP Codes
```python
zips = input("Enter ZIP codes (5-digit): ").split()
valid = list(filter(
    lambda z: len(z) == 5 and z.isdigit(), 
    zips
))
print(f"Valid ZIPs: {valid}")
```

### 9. Convert Celsius to Fahrenheit (Positive Only)
```python
celsius = list(map(float, input("Enter °C values: ").split()))
fahrenheit = list(map(
    lambda c: round((c * 9/5) + 32, 1), 
    filter(lambda c: c >= -273.15, celsius)
))
print(f"°F values: {fahrenheit}")
```

### 10. Filter Valid Usernames
```python
names = input("Enter usernames (min 3 chars, alphanumeric): ").split()
valid = list(filter(
    lambda u: 3 <= len(u) <= 15 and u.isalnum(), 
    names
))
print(f"Valid usernames: {valid}")
```

### 11. Calculate BMI Categories
```python
data = input("Enter height(m) weight(kg) pairs: ").split()
pairs = [data[i:i+2] for i in range(0, len(data), 2)]
valid = list(filter(lambda hw: float(hw[0]) > 0 and float(hw[1]) > 0, pairs))
bmi = list(map(
    lambda hw: round(float(hw[1]) / (float(hw[0])**2), 1), 
    valid
))
categories = list(map(
    lambda b: "Underweight" if b < 18.5 else "Normal" if b < 25 else "Overweight",
    bmi
))
print(f"BMI Categories: {categories}")
```

### 12. Filter Future Dates
```python
from datetime import datetime
dates = input("Enter dates (YYYY-MM-DD): ").split()
today = datetime.now().date()
valid = list(filter(
    lambda d: len(d.split('-')) == 3, 
    dates
))
future = list(filter(
    lambda d: datetime.strptime(d, "%Y-%m-%d").date() > today, 
    valid
))
print(f"Future dates: {future}")
```

### 13. Process Valid RGB Values
```python
colors = input("Enter RGB triplets (0-255): ").split()
triplets = [colors[i:i+3] for i in range(0, len(colors), 3)]
valid = list(filter(
    lambda rgb: len(rgb) == 3 and all(0 <= int(c) <= 255 for c in rgb), 
    triplets
))
hex_vals = list(map(
    lambda rgb: f"#{int(rgb[0]):02X}{int(rgb[1]):02X}{int(rgb[2]):02X}",
    valid
))
print(f"Hex colors: {hex_vals}")
```

### 14. Filter Valid Credit Cards
```python
cards = input("Enter credit card numbers (16 digits): ").split()
valid = list(filter(
    lambda c: len(c) == 16 and c.isdigit() and c[0] in '3456', 
    cards
))
masked = list(map(
    lambda c: f"****-****-****-{c[-4:]}", 
    valid
))
print(f"Masked cards: {masked}")
```

### 15. Calculate Taxable Income
```python
incomes = list(map(float, input("Enter incomes ($): ").split()))
deductions = float(input("Deduction amount: "))
taxable = list(map(
    lambda i: max(0, i - deductions), 
    filter(lambda i: i > 0, incomes)
))
print(f"Taxable incomes: {taxable}")
```

### 16. Filter Valid Product Codes
```python
codes = input("Enter product codes (ABC-123): ").split()
valid = list(filter(
    lambda c: len(c) == 7 and c[3] == '-' and c[:3].isalpha() and c[4:].isdigit(), 
    codes
))
upper_codes = list(map(lambda c: c.upper(), valid))
print(f"Valid codes: {upper_codes}")
```

### 17. Process Student Grades
```python
grades = list(map(float, input("Enter student grades (0-100): ").split()))
passed = list(filter(lambda g: 40 <= g <= 100, grades))
letter_grades = list(map(
    lambda g: 'A' if g >= 90 else 'B' if g >= 80 else 'C' if g >= 70 else 'D',
    passed
))
print(f"Passing letter grades: {letter_grades}")
```

### 18. Filter Valid IPv4 Addresses
```python
ips = input("Enter IP addresses: ").split()
valid = list(filter(
    lambda ip: all(0 <= int(octet) <= 255 for octet in ip.split('.') if octet.isdigit()) 
                and len(ip.split('.')) == 4,
    ips
))
private = list(filter(
    lambda ip: ip.startswith(('10.', '192.168.', '172.16.')), 
    valid
))
print(f"Private IPs: {private}")
```

### 19. Process Currency Exchange
```python
amounts = list(map(float, input("Enter USD amounts: ").split()))
rate = float(input("Exchange rate (USD to EUR): "))
valid = list(filter(lambda a: a > 0, amounts))
euros = list(map(lambda a: round(a * rate, 2), valid))
print(f"EUR amounts: {euros}")
```

### 20. Filter Valid ISBN-10 Numbers
```python
isbns = input("Enter ISBN-10 numbers: ").split()
def validate_isbn(isbn):
    if len(isbn) != 10 or not isbn[:-1].isdigit(): return False
    total = sum((i+1)*int(d) for i, d in enumerate(isbn[:9]))
    check = 'X' if total % 11 == 10 else str(total % 11)
    return check == isbn[9]

valid = list(filter(validate_isbn, isbns))
years = list(map(lambda isbn: "20" + isbn[4:6] if isbn[4:6] != "00" else "19" + isbn[4:6], valid))
print(f"Publication years: {years}")
```
