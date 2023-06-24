numbers = [15, -25, 0, 45, 34, 0, -6, -23]

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

total_count = len(numbers)
positive_ratio = positive_count / total_count
negative_ratio = negative_count / total_count
zero_ratio = zero_count / total_count

print("Positive ratio:", positive_ratio)
print("Negative ratio:", negative_ratio)
print("Zero ratio:", zero_ratio)
