from Prac07.guitar import Guitar

def main():

    i = 0
    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar(name, year, cost))
        print(guitars[i])
        i += 1


    # gibson = Guitar("Gibson", 2011, 16035.4)
    # print(gibson)
    # print(gibson.get_age())
    # print(gibson.is_vintage())

main()