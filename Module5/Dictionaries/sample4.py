squares = {x: x**2 for x in range(5)}
odds_only = {x: x**2 for x in range(10) if x % 2 != 0}
print(squares)     # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(odds_only)   # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}