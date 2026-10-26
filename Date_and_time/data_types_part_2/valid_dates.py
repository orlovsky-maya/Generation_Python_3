from datetime import date


def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except ValueError:
        return False

count = 0
while True:
    data = str(input())
    if data == "end":
        break
    else:
        day, month, year = map(int, data.split("."))
        if is_correct(day, month, year):
            count += 1
            print("Корректная")
        else:
            print("Некорректная")

print(count)

# Входные данные1
# 19.05.2016
# 05.13.2010
# 21.12.2012
# 01.01.1000
# 32.04.2003
# end
# Выходные данные1
# Корректная
# Некорректная
# Корректная
# Корректная
# Некорректная
# 3
# Входные данные2
# 15.02.1524
# 29.02.2017
# 27.05.1528
# 13.10.1736
# 40.06.431
# 31.07.5200
# 29.02.2016
# end
# Выходные данные2
# Корректная
# Некорректная
# Корректная
# Корректная
# Некорректная
# Корректная
# Корректная
# 5
