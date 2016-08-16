"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: ".format(str(len(password)),password))


def is_valid_password(password):

    if len(password) < 2 or len(password) > 6:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif 47 < ord(char) < 58:
            count_digit += 1
        elif char in SPECIALS:
            count_special += 1
        else:
            return False
        pass

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    # if we get here (without having returned False), then the password must be valid
    return True

main()