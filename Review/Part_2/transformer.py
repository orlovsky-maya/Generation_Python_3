n, x, y, a, b = [int(i) - 1 for i in input().split()]
nums = [i for i in range(1, n + 2)]
start_end = ((x, y), (a, b))
result = []
for s, e in start_end:
    pref = nums[0: s]
    result.extend(pref)
    rev = nums[s: e + 1]
    rev.reverse()
    result.extend(rev)
    suf = nums[e + 1:]
    result.extend(suf)
    nums = result
    result = []
print(*nums)


# Second solution
# n, x, y, a, b = [int(i) - 1 for i in input().split()]
# nums = [i for i in range(1, n + 2)]
#
# nums[x: y + 1] = nums[x:y + 1][::-1]
# nums[a: b + 1] = nums[a:b + 1][::-1]
# print(nums)

# n, x, y, a, b = [int(i) for i in input().split()]
# nums = list(range(1, n + 1))
#
# nums[x - 1:y] = reversed(nums[x - 1:y])
# nums[a - 1:b] = reversed(nums[a - 1:b])
#
# print(*nums)


# # INPUT DATA:
#
# # TEST_1:
# 9 2 5 6 9
#
# # TEST_2:
# 9 3 6 5 8
#
# # TEST_3:
# 5 1 3 4 5
#
# # TEST_4:
# 15 1 6 7 9
#
# # TEST_5:
# 8 3 4 6 8
#
# # TEST_6:
# 4 1 3 2 4
#
# # TEST_7:
# 9 5 7 1 8
#
# # TEST_8:
# 3 1 2 1 3
#
# # TEST_9:
# 5 1 3 1 3
#
# # TEST_10:
# 2 1 2 1 2
#
# # TEST_11:
# 3 1 2 2 3


# # OUTPUT DATA:
#
# # TEST_1:
# 1 5 4 3 2 9 8 7 6
#
# # TEST_2:
# 1 2 6 5 8 7 3 4 9
#
# # TEST_3:
# 3 2 1 5 4
#
# # TEST_4:
# 6 5 4 3 2 1 9 8 7 10 11 12 13 14 15
#
# # TEST_5:
# 1 2 4 3 5 8 7 6
#
# # TEST_6:
# 3 4 1 2
#
# # TEST_7:
# 8 5 6 7 4 3 2 1 9
#
# # TEST_8:
# 3 1 2
#
# # TEST_9:
# 1 2 3 4 5
#
# # TEST_10:
# 1 2
#
# # TEST_11:
# 2 3 1