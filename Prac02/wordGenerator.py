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

# word_format = (input("Please enter word format:\n\t'c' for consonants\n\t'v' for vowels\n> ")).lower()
word_length = int(input("Please enter desired length of word: "))
word_format = ""

for i in range(1, word_length + 1):
    word_format += random.choice(FORMAT_OPTIONS)

print("\nGenerated word format: ", word_format)

word = ""

for kind in word_format:
    if kind == "c" or kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "v" or kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(ALPHABET)
    else:
        word += kind

print("Generated word: ", word)