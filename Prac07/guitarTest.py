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
        if guitar_object.is_vintage():
            guitars.append([Guitar(name, year, cost), "Y"])
        else:
            guitars.append([Guitar(name, year, cost), "N"])
        print(guitar_object)
        i += 1

    print("These are my guitars:")
    for guitar_number in range(0,len(guitars)):
        if guitars[guitar_number][1] == "Y":
            print("Guitar {}: {:>25} ({}), worth ${:>12,.2f} (vintage)".format(guitar_number + 1,
                                                                              guitars[guitar_number][0].name,
                                                                              guitars[guitar_number][0].year,
                                                                              guitars[guitar_number][0].cost))
        else:
            print("Guitar {}: {:>25} ({}), worth ${:>12,.2f}".format(guitar_number + 1, guitars[guitar_number][0].name,
                                                                    guitars[guitar_number][0].year,
                                                                    guitars[guitar_number][0].cost))


    # gibson = Guitar("Gibson", 2011, 16035.4)
    # print(gibson)
    # print(gibson.get_age())
    # print(gibson.is_vintage())

main()