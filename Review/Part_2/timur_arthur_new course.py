d1, d2, d3 = int(input()), int(input()), int(input())
result = 0
minimum_shop1 = min(d1, d2)
result += minimum_shop1
minimum_shop2 = min(d3, d1 + d2)
result += minimum_shop2
minimum_home = min(max(d1, d2), d3 + minimum_shop1)
result += minimum_home
print(result)

# # INPUT DATA:
#
# # TEST_1:
# 10
# 20
# 30
#
# # TEST_2:
# 10
# 10
# 45
#
# # TEST_3:
# 100
# 33
# 34
#
# # TEST_4:
# 777
# 777
# 777
#
# # TEST_5:
# 2
# 2
# 8
#
# # TEST_6:
# 12
# 34
# 56
#
# # TEST_7:
# 789
# 101112
# 131415
#
# # TEST_8:
# 27485716
# 99999999
# 35182
#
# # TEST_9:
# 1
# 293548
# 5
#
# # TEST_10:
# 12059
# 259855
# 5874875
#
# # TEST_11:
# 46981
# 105809
# 585858
#
# # TEST_12:
# 9889
# 1221
# 2442
#
# # TEST_13:
# 100500
# 200600
# 300700
#
# # TEST_14:
# 318476
# 318476
# 318476
#
# # TEST_15:
# 23985
# 3353
# 75633
#
# # TEST_16:
# 120
# 1298
# 2222
#
# # TEST_17:
# 98437
# 23487
# 666672
#
# # TEST_18:
# 100000000
# 100000000
# 100000000
#
# # TEST_19:
# 2
# 5
# 2
#
# # TEST_20:
# 1
# 1000
# 1
#
# # TEST_21:
# 1
# 100000000
# 1


# # OUTPUT DATA:
#
# # TEST_1:
# 60
#
# # TEST_2:
# 40
#
# # TEST_3:
# 134
#
# # TEST_4:
# 2331
#
# # TEST_5:
# 8
#
# # TEST_6:
# 92
#
# # TEST_7:
# 203802
#
# # TEST_8:
# 55041796
#
# # TEST_9:
# 12
#
# # TEST_10:
# 543828
#
# # TEST_11:
# 305580
#
# # TEST_12:
# 7326
#
# # TEST_13:
# 601800
#
# # TEST_14:
# 955428
#
# # TEST_15:
# 54676
#
# # TEST_16:
# 2836
#
# # TEST_17:
# 243848
#
# # TEST_18:
# 300000000
#
# # TEST_19:
# 8
#
# # TEST_20:
# 4
#
# # TEST_21:
# 4
