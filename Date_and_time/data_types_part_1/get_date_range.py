from datetime import date


def get_date_range(start: date, end: date) -> list:
    if start > end:
        return list()
    else:
        l = list(range(start.toordinal(), end.toordinal() + 1))
        return list(map(date.fromordinal, l))


# Входные данные1
date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
# print(get_date_range(date1, date2))
# Выходные данные1
# 2021-10-01
# 2021-10-02
# 2021-10-03
# 2021-10-04
# 2021-10-05


# Входные данные2
date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))
# Выходные данные2
# [datetime.date(2019, 6, 5)]