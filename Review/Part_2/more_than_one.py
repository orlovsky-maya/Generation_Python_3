s = [int(i) for i in input().split()]
print(*sorted(set(filter(lambda x: s.count(x) > 1, s))))


# # INPUT DATA:
#
# # TEST_1:
# 4 8 0 3 4 2 0 3
#
# # TEST_2:
# 1 2 3 4 5 4 5 6 7 7 7 7 4 4
#
# # TEST_3:
# 1 2 3 4 5 6 7 8 9
#
# # TEST_4:
# 3 3
#
# # TEST_5:
# 0
#
# # TEST_6:
# 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
#
# # TEST_7:
# 5 55 3 3 0 0
#
# # TEST_8:
# 3 1 3 2 3 11 4 3 5 3 6 3 7 3 8 3 9 3 10 3 11 3 3 12 13 1


# # OUTPUT DATA:
#
# # TEST_1:
# 0 3 4
#
# # TEST_2:
# 4 5 7
#
# # TEST_3:
#
#
# # TEST_4:
# 3
#
# # TEST_5:
#
#
# # TEST_6:
# 5
#
# # TEST_7:
# 0 3
#
# # TEST_8:
# 1 3 11