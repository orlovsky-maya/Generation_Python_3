letters = [input() for _ in range(3)]
r = "АаВСсЕеНКМОоРрТХху"
e = "AaBCcEeHKMOoPpTXxy"

ru = 0
en = 0
for l in letters:
    if l in r:
        ru += 1
    else:
        en += 1
if ru == 3:
    print("ru")
elif en == 3:
    print("en")
else:
    print("mix")



# Optimal solution

langs = ['ru', 'mix', 'mix', 'en']
eng = 'AaBCcEeHKMOoPpTXxy'
ind = sum(input() in eng for _ in range(3))
print(langs[ind])

#
# # INPUT DATA:
#
# # TEST_1:
# Р
# О
# А
#
# # TEST_2:
# o
# K
# M
#
# # TEST_3:
# T
# а
# B
#
# # TEST_4:
# а
# К
# о
#
# # TEST_5:
# E
# c
# T
#
# # TEST_6:
# H
# Н
# B
#
# # TEST_7:
# H
# p
# T
#
# # TEST_8:
# Н
# р
# Т
#
# # TEST_9:
# р
# р
# p
#
# # TEST_10:
# а
# а
# а
#
# # TEST_11:
# x
# x
# x
#
#
# # OUTPUT DATA:
#
# # TEST_1:
# ru
#
# # TEST_2:
# en
#
# # TEST_3:
# mix
#
# # TEST_4:
# ru
#
# # TEST_5:
# en
#
# # TEST_6:
# mix
#
# # TEST_7:
# en
#
# # TEST_8:
# ru
#
# # TEST_9:
# mix
#
# # TEST_10:
# ru
#
# # TEST_11:
# en