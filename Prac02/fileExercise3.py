in_file = open("numbers.txt", "r")
lines = in_file.readlines()

line_one = int(lines[0])
line_two = int(lines[1])

sum = line_one + line_two
print(sum)

in_file.close()