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
        guitar_object = Guitar(name, year, cost)
        guitars.append(guitar_object)
        print(guitar_object)
        i += 1

    print("These are my guitars:")
    for guitar_number in range(0,len(guitars)):
        if guitars[guitar_number].is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""

        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(guitar_number + 1,
                                                                           guitars[guitar_number].name,
                                                                           guitars[guitar_number].year,
                                                                           guitars[guitar_number].cost, vintage_string))

main()
