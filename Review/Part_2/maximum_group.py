n = int(input())

if n < 10:
    print(1)
else:
    nums = [i for i in range(10, n + 1)]
    dic_nums = dict([(i, 1)for i in range(1, 10)])
    for num in nums:
        summa = sum([int(i) for i in str(num)])
        dic_nums[summa] = dic_nums.get(summa, 0) + 1
    print(max(dic_nums.values()))

# # INPUT DATA:
#
# # TEST_1:
# 13
#
# # TEST_2:
# 2
#
# # TEST_3:
# 20
#
# # TEST_4:
# 100
#
# # TEST_5:
# 200
#
# # TEST_6:
# 69
#
# # TEST_7:
# 1337
#
# # TEST_8:
# 3
#
# # TEST_9:
# 4
#
# # TEST_10:
# 10
#
# # TEST_11:
# 999

# # OUTPUT DATA:
#
# # TEST_1:
# 2
#
# # TEST_2:
# 1
#
# # TEST_3:
# 3
#
# # TEST_4:
# 10
#
# # TEST_5:
# 19
#
# # TEST_6:
# 7
#
# # TEST_7:
# 104
#
# # TEST_8:
# 1
#
# # TEST_9:
# 1
#
# # TEST_10:
# 2
#
# # TEST_11:
# 75


