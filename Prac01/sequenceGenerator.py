x = int(input("Please enter 1st boundary value: "))
y = int(input("Please enter 2nd boundary value: "))

if y < x:
    x,y = y,x

print("(1): Even numbers from 1st to 2nd boundary\n(2): Odd numbers from 1st to 2nd boundary\n(3): Squares from 1st to 2nd boundary\n(4): Exit")
choice = input("Please enter a menu option: ")

while choice != "4":
    if choice == "1":
        for i in range (x,y + 1):
            if i%2 == 0:
                print(i, end=' ')
    elif choice == "2":
        for i in range (x,y + 1):
            if i%2 != 0:
                print(i, end=' ')
    elif choice == "3":
        for i in range (x,y + 1):
                print(i**2, end=' ')
    else:
        print("Invalid menu option\n")

    print("\n\n(1): Even numbers from 1st to 2nd boundary\n(2): Odd numbers from 1st to 2nd boundary\n(3): Squares from 1st to 2nd boundary\n(4): Exit")
    choice = input("Please enter a menu option: ")

print("Program complete.")