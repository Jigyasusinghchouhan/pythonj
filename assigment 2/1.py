name = input("Enter your name: ")

name_length = 0
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


for letter in name:

    name_length += 1

    if letter.lower() in vowel_count:
        vowel_count[letter.lower()] += 1


print("There are", name_length, "characters in your name. :")
for vowel, count in vowel_count.items():
    print(" The Number of times", vowel, "occurs in your name:", count)
