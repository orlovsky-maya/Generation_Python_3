def is_valid(pin):
    if not pin.isdigit() or len(pin) not in (4, 5, 6):
        return False
    else:
        return True


# INPUT DATA:

# TEST_1:
print(is_valid('4367'))

# TEST_2:
print(is_valid('92134'))

# TEST_3:
print(is_valid('89abc1'))

# TEST_4:
print(is_valid('900876'))

# TEST_5:
print(is_valid('49 83'))

# TEST_6:
print(is_valid('467'))

# TEST_7:
print(is_valid('4323423424467'))

# TEST_8:
print(is_valid('3 7 0'))

# TEST_9:
print(is_valid('0000'))

# TEST_10:
print(is_valid(''))

# TEST_11:
print(is_valid('aaaa'))

# # OUTPUT DATA:
#
# # TEST_1:
# True
#
# # TEST_2:
# True
#
# # TEST_3:
# False
#
# # TEST_4:
# True
#
# # TEST_5:
# False
#
# # TEST_6:
# False
#
# # TEST_7:
# False
#
# # TEST_8:
# False
#
# # TEST_9:
# True
#
# # TEST_10:
# False
#
# # TEST_11:
# False
