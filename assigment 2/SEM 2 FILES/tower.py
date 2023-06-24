
list_0 = [1, 3, 6, 7, 8, 9, 10, 2, 3, 4]
list_1 = [12, 56, 3, 78, 34, 56, 2, 10]
list_2 = [123, 567, 234, 890]
list_3 = [5, 7, 8, 9, 3, -2, -4, -2, 5, 6, 8, 11, 2]

def maximum(L):
    biggest_item = L[0]
    for item in L:
        if item > biggest_item:
            biggest_item = item
    return item

def rec_max(L):
    if L[1:]:
        recursed_max = rec_max(L[1:])
        if L[0] > recursed_max:
            return L[0]
        else:
            return recursed_max 
    elif not L:
        return
    else:
        return L[0]

# Tests
print("maximum(list_0)", maximum(list_0))
print("maximum(list_1)", maximum(list_1))
print("maximum(list_2)", maximum(list_2))
print("maximum(list_3)", maximum(list_3))