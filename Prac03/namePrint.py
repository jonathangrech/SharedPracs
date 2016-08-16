def main():
    name = get_name()

    while not name:
        name = input("Name cannot be blank. Please enter your name: ")

    frequency = int(input("Please enter frequency value: "))

    print_characters(name,frequency)


def print_characters(name, frequency):

    for char in range(frequency - 1, len(name), frequency):
        print(name[char])


def get_name():
    name = input("Please enter your name: ")
    return name

main()