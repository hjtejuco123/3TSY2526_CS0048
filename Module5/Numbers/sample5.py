from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction('1.5')  # Preferred over float instantiation
print(f1 + f2)  # Outputs: 11/6