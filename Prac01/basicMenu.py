name = input("Please enter your name: ")
print("(H)ello\n(G)oodbye\n(Q)uit\n")
choice = input("Please enter a menu option: ")
choice = str.upper(choice)

while choice != "Q":
    if choice == "H":
        print("Hello " + name)
    elif choice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid menu option\n")

    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    choice = input("Please enter a menu option: ")
    choice = str.upper(choice)

print("Program complete.")
