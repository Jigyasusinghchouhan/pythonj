numbers = [10, 20, 30, 20, 20]
setlist = set(numbers)

for element in setlist:

    frequency = numbers.count(element)

    print('element =', element, 'frequency :', frequency)