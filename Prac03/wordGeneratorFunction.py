"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FORMAT_OPTIONS = "cv#%*"

def main():
    word_format = (input("Please enter word format:\n\t'c' for consonants\n\t'v' for vowels\n> ")).lower()

    validity = False

    while validity == False:
        validity = is_valid_format(word_format)
        if validity == False:
            word_format = (input("Word format can only consist of:\n\t'c' for consonants\n\t'v' for vowels\n> ")).lower()

    word = ""

    for kind in word_format:
        if kind == "c" or kind == "%":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print("Generated word: ", word)


def is_valid_format(word_format):
    for kind in word_format:
        if kind != "c" and kind != "v":
            return False

    return True


main()