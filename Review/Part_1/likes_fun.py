def likes(names):
    count_names = len(names)
    if count_names == 0:
        return "Никто не оценил данную запись"
    elif count_names == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif count_names == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif count_names == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    elif count_names > 3:
        return f"{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись"


# INPUT DATA:

# TEST_1:
print(likes(['Дима', 'Алиса']))

# TEST_2:
print(likes(['Эндрю', 'Тоби', 'Том']))

# TEST_3:
print(likes([]))

# TEST_4:
print(likes(['Том']))

# TEST_5:
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))

# TEST_6:
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур', 'Тимур']))

# TEST_7:
print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))

# TEST_8:
names = [str(i) * 3 for i in range(100)]
print(likes(names))


# # OUTPUT DATA:
#
# # TEST_1:
# Дима и Алиса оценили данную запись
#
# # TEST_2:
# Эндрю, Тоби и Том оценили данную запись
#
# # TEST_3:
# Никто не оценил данную запись
#
# # TEST_4:
# Том оценил(а) данную запись
#
# # TEST_5:
# Эндрю, Тоби и 2 других оценили данную запись
#
# # TEST_6:
# Эндрю, Тоби и 3 других оценили данную запись
#
# # TEST_7:
# Артур, Тимур и 4 других оценили данную запись
#
# # TEST_8:
# 000, 111 и 98 других оценили данную запись