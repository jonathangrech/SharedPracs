import random

number_of_lines = int(input("How many quick picks? "))

for i in range(0,number_of_lines):
    list = []
    taken_numbers = []
    while len(list) < 6:
        number = random.randint(1,10)
        if number not in taken_numbers:
            taken_numbers.append(number)
            list.append(number)
    print(list)