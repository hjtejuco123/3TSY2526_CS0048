data = {"a": 1, "b": 2, "c": 3}
val = data.pop("b")      # Removes 'b', returns 2
item = data.popitem()    # Removes & returns arbitrary pair
data.clear()             # Empties dictionary
print(val, data)