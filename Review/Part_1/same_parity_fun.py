def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def same_parity(numbers):
    result = []
    for n in numbers:
        if is_even(numbers[0]):
            if is_even(n):
                result.append(n)
        else:
            if not is_even(n):
                result.append(n)
    return result


# Alternative solution
# def same_parity(numbers):
#     if len(numbers) > 0:
#         if is_even(numbers[0]):
#             return list(filter(lambda num: num % 2 == 0, numbers))
#         else:
#             return list(filter(lambda num: num % 2 != 0, numbers))
#     else:
#         return []


# INPUT DATA:

# TEST_1:
print(same_parity([]))

# TEST_2:
print(same_parity([6, 0, 67, -7, 10, -20]))

# TEST_3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

# TEST_4:
print(same_parity([2]))

# TEST_5:
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))

# TEST_6:
print(same_parity([-1, 1248234832443, 8]))

# TEST_7:
print(same_parity([1, 2, 4, 6, 8]))

# TEST_8:
print(same_parity([1, 3, 5, 7, 9]))

# # OUTPUT DATA:
#
# # TEST_1:
# []
#
# # TEST_2:
# [6, 0, 10, -20]
#
# # TEST_3:
# [-7, 67, -9, -29]
#
# # TEST_4:
# [2]
#
# # TEST_5:
# [2, 2, 2, 2, 0, 2]
#
# # TEST_6:
# [-1, 1248234832443]
#
# # TEST_7:
# [1]
#
# # TEST_8:
# [1, 3, 5, 7, 9]
