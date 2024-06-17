def choose_plural(amount, declensions):
    suffixes = {
        1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 0: 2,
    }
    num = amount % 100
    if num > 20:
        num = num % 10
    suf = suffixes[num]
    return f'{amount} {declensions[suf]}'


# INPUT DATA:

# TEST_1:
print(choose_plural(21, ('пример', 'примера', 'примеров')))

# TEST_2:
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

# TEST_3:
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

# TEST_4:
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))

# TEST_5:
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))

# TEST_6:
print(choose_plural(512312, ('цент', 'цента', 'центов')))

# TEST_7:
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))

# TEST_8:
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))

# TEST_9:
print(choose_plural(240, ('курица', 'курицы', 'куриц')))

# TEST_10:
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))

# TEST_11:
print(choose_plural(505, ('утка', 'утки', 'уток')))

# TEST_12:
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))

# TEST_13:
print(choose_plural(11, ('стул', 'стула', 'стульев')))

# TEST_14:
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))

# TEST_15:
print(choose_plural(2, ('пример', 'примера', 'примеров')))

# TEST_16:
print(choose_plural(111, ('пример', 'примера', 'примеров')))

# TEST_17:
print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))


# # OUTPUT DATA:
#
# # TEST_1:
# 21 пример
#
# # TEST_2:
# 92 гвоздя
#
# # TEST_3:
# 8 яблок
#
# # TEST_4:
# 111223 копейки
#
# # TEST_5:
# 763434 рубля
#
# # TEST_6:
# 512312 центов
#
# # TEST_7:
# 59 помидоров
#
# # TEST_8:
# 23424157 огурцов
#
# # TEST_9:
# 240 куриц
#
# # TEST_10:
# 49324 плюмбуса
#
# # TEST_11:
# 505 уток
#
# # TEST_12:
# 666 шкафов
#
# # TEST_13:
# 11 стульев
#
# # TEST_14:
# 3458438435812 долларов
#
# # TEST_15:
# 2 примера
#
# # TEST_16:
# 111 примеров
#
# # TEST_17:
# 1223123111 примеров
