num = input("Enter your number: ")

numbers = num.split('00') 
even_numbers = []

for number in numbers:
    if number != '':
        for digit in number:
            if int(digit) % 2 == 0:
                even_numbers.append(int(digit))

if even_numbers:
    sum_even = sum(even_numbers)
    avg_even = sum_even / len(even_numbers)
    print("The summation of even numbers is: {}".format("+".join(map(str, even_numbers))), end="=")
    print(sum_even)
    print("The average is: {:.1f}".format(avg_even))
else:
    print("There are no even numbers in the input.")
