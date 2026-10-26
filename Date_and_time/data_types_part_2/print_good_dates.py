from datetime import date


def print_good_dates(dates: list[date]):
    for d in sorted(dates):
        if d.year == 1992 and (int(d.month) + int(d.day)) == 29:
            print(d.strftime('%B %d, %Y'))

# Входные данные1
dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
# Выходные данные1
# September 20, 1992
# October 19, 1992


# Входные данные2
# dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
# print_good_dates(dates)
# Выходные данные2