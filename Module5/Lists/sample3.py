lst = [1, 2]
lst.append(3)
lst.extend([4, 5])
lst.pop()      # Removes last item
lst.remove(2)  # Removes value 2
print(lst)     # Outputs: [1, 3, 4]