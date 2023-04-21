size = int(input("Enter the size of the triangle: "))

for i in range(size, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
