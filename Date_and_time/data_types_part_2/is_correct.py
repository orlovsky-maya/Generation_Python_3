from datetime import date


def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except ValueError:
        return False
# Входные данные1
print(is_correct(31, 12, 2021))
# Выходные данные1
# True
# Входные данные2
print(is_correct(31, 13, 2021))
# Выходные данные2
# False