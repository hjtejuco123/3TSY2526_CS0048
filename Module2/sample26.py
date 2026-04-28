# Nested Loops

#Create a 5x5 multiplication table
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i*j}", end="\t")
#     print()  # New line after each row


# Print a right triangle pattern
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


# Initialize and print a 3x3 matrix
# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(i * 3 + j + 1)
#     matrix.append(row)

# # # Print the matrix
# # for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()

# Find all pairs that sum to a target value
# numbers = [1, 2, 3, 4, 5]
# target = 7

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(f"Pair found: {numbers[i]} + {numbers[j]} = {target}")

# find all the sum of 7 in the list
# Pair: 1+2 = 3 (does not match the target) 
# Pair: 2+3 = 5 (does not match the target)
# Pair: 3+4 = 7 (matches the target)
# Pair: 4+5 = 9 (does not match the target)
# Pair Found : 3 + 4 = 7 (matches the target)
# Pair Found : 5 + 2 = 7 (matches the target)

# numbers = [1, 2, 3, 4, 5]
# target = 7

# print(f"Finding pairs that sum to {target} in the list: {numbers}")
# print("-" * 40)

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         current_sum = numbers[i] + numbers[j]
        
#         # Always show the pair, but indicate if it matches the target
#         if current_sum == target:
#             print(f"x Pair found: {numbers[i]} + {numbers[j]} = {current_sum} (matches target)")
#         else:
#             print(f"Pair: {numbers[i]} + {numbers[j]} = {current_sum} (does not match target)")
            
# # Check if any pairs were found
# pairs_found = False
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             pairs_found = True
#             break
#     if pairs_found:
#         break

# print("\n" + "-" * 40)
# if pairs_found:
#     print(f"Result: There are pairs in the list that sum to {target}")
# else:
#     print(f"Result: No pairs in the list sum to {target}")


# Search for a value in a 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# target = 5
# found = False

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == target:
#             print(f"Found {target} at position ({i}, {j})")
#             found = True
#             break
#     if found:
#         break