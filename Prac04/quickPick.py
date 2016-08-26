import random

number_of_lines = int(input("How many quick picks? "))

for i in range(0,number_of_lines):
    list_of_numbers = []
    taken_numbers = []
    while len(list_of_numbers) < 6:
        number = random.randint(1,10)
        if number not in taken_numbers:
            taken_numbers.append(number)
            list_of_numbers.append(number)

    print(" ".join(str(x) for x in sorted(list_of_numbers)))