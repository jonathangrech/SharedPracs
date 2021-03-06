"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def phrase_as_sentence(phrase):
    """
    >>> phrase_as_sentence("hello") == "Hello."
    True
    >>> phrase_as_sentence("It is an ex parrot.") == "It is an ex parrot."
    True
    >>> phrase_as_sentence("   hello world   ") == "Hello world."
    True

    """
    final_character = "."
    if phrase.strip()[-1] == ".":
        final_character = ""
    return phrase.strip()[0].upper() + phrase.strip()[1:] + final_character


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0

    # Note that Car's __init__ function sets the fuel in one of two ways: using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function (don't change the tests, but the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence - starting with a capital and ending with a single full stop
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass