"""
CP1404/CP5632 Practical
Recursion
"""


# def do_it(n):
#     if n <= 0:
#         return 0
#     return n % 2 + do_it(n - 1)
#
# print(do_it(5))


def do_something(n):
    if n < 0:
        return 0
    else:
        print(n ** 2)
        do_something(n-1)

do_something(4)
