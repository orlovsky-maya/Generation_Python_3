from datetime import date

date_1 = input()
date_2 = input()
min_date = min(date_1, date_2)
print(date.fromisoformat(min_date).strftime('%d-%m (%Y)'))
