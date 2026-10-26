from datetime import date


def get_min_max(dates: [date, date]) -> tuple[date, date]:
    if dates:
        min_date = min(dates)
        max_date = max(dates)
        return min_date, max_date
    else:
        return tuple()


# Входные данные1
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

print(get_min_max(dates))


# Выходные данные1
# (datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))

# Входные данные2
print(get_min_max([]))
# Выходные данные2
# ()