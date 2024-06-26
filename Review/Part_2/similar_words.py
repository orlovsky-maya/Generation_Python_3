word = input()
words = [input() for _ in range(int(input()))]
vowels = "ауоыиэяюёе"
word_num = ''.join(list(map(lambda l: "0" if l in vowels else "1", word)))
index_vol = word_num.rfind('0')
word_num = word_num[:index_vol + 1]
for w in words:
    w_num = ''.join(list(map(lambda l: "0" if l in vowels else "1", w)))
    ind_v = w_num.rfind('0')
    w_num = w_num[:ind_v + 1]
    if word_num == w_num:
        print(w)
    else:
        continue


# Second solution

vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
pattern = [i for i, c in enumerate(input()) if c in vowels]

for _ in range(int(input())):
    word = input()
    if [i for i, c in enumerate(word) if c in vowels] == pattern:
        print(word)

# # INPUT DATA:
#
# # TEST_1:
# машина
# 8
# сеть
# машинист
# дорога
# урок
# работа
# аксиома
# железо
# ветеран
#
# # TEST_2:
# весть
# 3
# месть
# гость
# лань
#
# # TEST_3:
# внук
# 5
# брат
# дом
# ворон
# сват
# обед
#
# # TEST_4:
# кузина
# 9
# курс
# низина
# рябина
# регион
# спина
# пружина
# лавина
# дубина
# древесина
#
# # TEST_5:
# море
# 5
# моряк
# стол
# стул
# пирог
# вода
#
# # TEST_6:
# шорох
# 3
# топот
# шалаш
# пейзаж
#
# # TEST_7:
# розжиг
# 3
# светофор
# фанта
# тростник
#
# # TEST_8:
# фигура
# 5
# машинаннннн
# ржавчина
# граль
# река
# полинанннннннннн


# # OUTPUT DATA:
#
# # TEST_1:
# машинист
# дорога
# работа
# железо
# ветеран
#
# # TEST_2:
# месть
# гость
# лань
#
# # TEST_3:
# брат
# сват
#
# # TEST_4:
# низина
# рябина
# лавина
# дубина
#
# # TEST_5:
# моряк
# пирог
# вода
#
# # TEST_6:
# топот
# шалаш
#
# # TEST_7:
# фанта
#
# # TEST_8:
# машинаннннн
# полинанннннннннн
