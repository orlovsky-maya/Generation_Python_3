def convert(string):
    lowercase = 0
    uppercase = 0
    for i in string:
        if i.islower():
            lowercase += 1
        elif i.isupper():
            uppercase += 1
    if lowercase >= uppercase:
        return string.lower()
    else:
        return string.upper()



# INPUT DATA:

# TEST_1:
print(convert('BEEgeek'))

# TEST_2:
print(convert('pyTHON'))

# TEST_3:
print(convert('pi31415!'))

# TEST_4:
print(convert('ABCDEF'))

# TEST_5:
print(convert('abcdef'))

# TEST_6:
print(convert('12345!?'))

# TEST_7:
print(convert('PI31415!'))

# TEST_8:
print(convert('ABCdef'))

# TEST_9:
print(convert('ABCdef123'))

# TEST_10:
print(convert('AbCdEf12345'))

# TEST_11:
print(convert('dEfAbC'))

# # OUTPUT DATA:
#
# # TEST_1:
# beegeek
#
# # TEST_2:
# PYTHON
#
# # TEST_3:
# pi31415!
#
# # TEST_4:
# ABCDEF
#
# # TEST_5:
# abcdef
#
# # TEST_6:
# 12345!?
#
# # TEST_7:
# PI31415!
#
# # TEST_8:
# abcdef
#
# # TEST_9:
# abcdef123
#
# # TEST_10:
# abcdef12345
#
# # TEST_11:
# defabc