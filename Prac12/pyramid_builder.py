# Iterative solution
#
#
# def get_blocks_iteratively(n):
#     number_of_blocks = 0
#     for i in range(n, 0, -1):
#         number_of_blocks += i
#     return number_of_blocks
#
# print(get_blocks_iteratively(6))

# Recursive solution

def get_blocks_recursively(n):
    if n <= 0:
        return 0
    return n + get_blocks_recursively(n-1)

print(get_blocks_recursively(7))