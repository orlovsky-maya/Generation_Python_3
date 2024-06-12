def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    elif number in numbers:
        return numbers.index(number)
    elif number == 0:
        closest_num = sorted(numbers)[0]
        return numbers.index(closest_num)
    else:
        numbers_copy = numbers.copy()
        numbers_copy.append(number)
        sorted_nums = sorted(numbers_copy)
        ind_num = sorted_nums.index(number)
        if ind_num == 0:
            closest_num = sorted_nums[1]
            return numbers.index(closest_num)
        elif ind_num == len(numbers_copy) - 1:
            closest_num = sorted_nums[-2]
            return numbers.index(closest_num)
        else:
            num1 = sorted_nums[ind_num - 1]
            num2 = sorted_nums[ind_num + 1]
            ind_num1 = numbers.index(num1)
            ind_num2 = numbers.index(num2)
            dif1 = abs(number - num1)
            dif2 = abs(number - num2)
            if dif1 == dif2:
                return min(ind_num1, ind_num2)
            elif dif1 < dif2:
                return ind_num1
            else:
                return ind_num2


# Optimal solution

# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1


# INPUT DATA:

# TEST_1:
print(index_of_nearest([], 17))

# TEST_2:
print(index_of_nearest([7, 13, 3, 5, 18], 0))

# TEST_3:
print(index_of_nearest([9, 5, 3, 2, 11], 4))

# TEST_4:
print(index_of_nearest([7, 5, 4, 4, 3], 4))

# TEST_5:
print(index_of_nearest([6, 100, 101, 2], 4))

# TEST_6:
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))

# TEST_7:
print(index_of_nearest([1, 14, 100, 65, 6], 5))

# TEST_8:
print(index_of_nearest([10, 164, 100, 265, 16], 8))

# TEST_9:
print(index_of_nearest([10, 99, 0, -12, 16], -9))

# TEST_10:
print(index_of_nearest([1, 1, 1, 1, 1], 1))

# # OUTPUT DATA:
#
# # TEST_1:
# -1
#
# # TEST_2:
# 2
#
# # TEST_3:
# 1
#
# # TEST_4:
# 2
#
# # TEST_5:
# 0
#
# # TEST_6:
# 3
#
# # TEST_7:
# 4
#
# # TEST_8:
# 0
#
# # TEST_9:
# 3
#
# # TEST_10:
# 0
