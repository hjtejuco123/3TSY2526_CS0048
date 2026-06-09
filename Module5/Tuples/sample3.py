t = (1, 2, [3, 4])
t[2].append(5)  # Allowed: nested list is mutable
# t[0] = 99     # Uncommenting raises TypeError
print(t)  # Outputs: (1, 2, [3, 4, 5])