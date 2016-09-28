from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar


def main():

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print("Current fare: ${}".format(taxi.get_fare()))

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Current fare: ${}".format(taxi.get_fare()))

    bad_car = UnreliableCar("Commodore", 100, 90)
    bad_car.drive(65)
    print(bad_car)

main()