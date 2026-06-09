scores = {"Math": 90, "Science": 85, "History": 92}
for key, val in scores.items():
    print(f"{key}: {val}")
print("All > 80?", all(v > 80 for v in scores.values()))