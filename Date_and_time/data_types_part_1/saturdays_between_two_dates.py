from datetime import date


def saturdays_between_two_dates(start: date, end: date) -> int:
    ccount_of_saturday = 0
    if start > end:
        l = list(range(end.toordinal(), start.toordinal() + 1))
    else:
        l = list(range(start.toordinal(), end.toordinal() + 1))
    dates = list(map(date.fromordinal, l))
    for d in dates:
        if d.isoweekday() == 6:
            ccount_of_saturday += 1
    return ccount_of_saturday

# Входные данные1
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
# Выходные данные1
# 3


# Входные данные2
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))
# Выходные данные2
# 4


# Входные данные3
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
# Выходные данные3
# 0

# Входные данные4
date1 = date(2010, 6, 13)
date2 = date(2011, 7, 14)
print(saturdays_between_two_dates(date1, date2))
# Выходные данные4
# 56


# TEST_7:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)
print(saturdays_between_two_dates(date1, date2))
# TEST_7:
# 1
