arr = [5, 7, 3, 4, 9]

for i in range(len(arr)):
    next_high = -1
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            next_high = arr[j]
            break
    print(next_high)
