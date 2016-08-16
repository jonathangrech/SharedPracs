try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Cannot divide by zero! Enter valid denominator: "))

    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")