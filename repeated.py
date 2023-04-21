list1 = [2, 3, 4, 4, 5, 5, 6]
list2 = [3, 4, 4, 4, 5, 7]
repeated = []

for x in repeated:
    count1 = list1.count(x)
    count2 = list2.count(x)
    for i in range(min(count1, count2)):
        repeated.append(x)
        