numbers = [45, 30, 23, 10, 67, 45]
min_sum = min(sum(numbers[:i]+numbers[i+1:]) for i in range(len(numbers)))
max_sum = max(sum(numbers[:i]+numbers[i+1:]) for i in range(len(numbers)))
print(f"Minimum sum: {min_sum}")
print(f"Maximum sum: {max_sum}")
