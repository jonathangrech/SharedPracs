from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu_option = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    total_bill = 0

    while menu_option != "q":
        if menu_option == "c":
            print("Taxis available:")
            for i in range (0,len(taxis)):
                print("{} - {}".format(i,taxis[i]))

            taxi_option = int(input("Choose taxi: "))

            print("Bill to date: ${:.2f}".format(total_bill))

            total_bill = taxis[0].get_fare() + (taxis[1].get_fare() + taxis[2].get_fare())


        elif menu_option == "d":
            drive_distance = float(input("Drive how far? "))
            initial_fuel = taxis[taxi_option].fuel
            try:
                actual_driven_distance = taxis[taxi_option].drive(drive_distance)
                cost_of_trip = taxis[taxi_option].get_trip_fare(actual_driven_distance, initial_fuel)
                print("Your {} trip cost you ${:.2f}".format(taxis[taxi_option].name, cost_of_trip))
                total_bill += cost_of_trip
                print("Bill to date: ${:.2f}".format(total_bill))
                # taxis[taxi_option].drive(drive_distance)
                # print("Your {} trip cost you ${:.2f}".format(taxis[taxi_option].name, taxis[taxi_option].get_trip_fare(drive_distance, initial_fuel)))
                #
                # total_bill += taxis[taxi_option].get_trip_fare(drive_distance, initial_fuel)
                # print("Bill to date: ${:.2f}".format(total_bill))


            except UnboundLocalError:
                print("Choose a taxi first")

        else:
            print("Invalid menu choice")

        menu_option = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    for i in range(0, len(taxis)):
        print("{} - {}".format(i, taxis[i]))

main()