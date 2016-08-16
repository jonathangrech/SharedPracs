name = input("Please enter your name: ")

while not name:
    name = input("Name cannot be blank. Please enter your name: ")

for char in range(1, len(name), 2):
    print(name[char])