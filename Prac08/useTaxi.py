from Prac08.taxi import Car
from Prac08.taxi import Taxi

def main():

    taxi = Taxi("Prius 1", 100, 1.2)
    taxi.drive(40)
    print(taxi)
    print("Current fare: ${}".format(taxi.get_fare()))

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Current fare: ${}".format(taxi.get_fare()))

main()