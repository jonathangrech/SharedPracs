def main():
    lower = 10
    upper = 100
    number = get_number(lower,upper)
    print("{} is valid".format(number))



def get_number(lower,upper):
    is_valid = False
    while not is_valid:
        try:
            num = int(input("Enter a number ({} - {}): ".format(lower, upper)))
            if num < lower or num > upper:
                print("Number must be within bounds")
            else:
                is_valid = True

        except ValueError:
            print("Not a number")

    return num

main()