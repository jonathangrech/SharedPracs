from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi


def main():

    # taxi = Taxi("Prius 1", 100)
    # taxi.drive(40)
    # print(taxi)
    # print("Current fare: ${}".format(taxi.get_fare()))
    #
    # taxi.start_fare()
    # taxi.drive(100)
    # print(taxi)
    # print("Current fare: ${}".format(taxi.get_fare()))
    #
    # bad_car = UnreliableCar("Commodore", 100, 90)
    # bad_car.drive(65)
    # print(bad_car)

    flash_car = SilverServiceTaxi("Hummer", 200, 2)
    flash_car.start_fare()

    flash_car.drive(10)
    print(flash_car)
    print("Current fare: ${}".format(flash_car.get_fare()))

main()