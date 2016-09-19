from Prac07.guitar import Guitar

def main():
    gibson = Guitar("Gibson", 2011, 16035.4)
    print(gibson)
    print(gibson.get_age())
    print(gibson.is_vintage())

main()