from datetime import date

n = int(input())
l = []
for i in range(n):
    num = date.fromisoformat(input())
    l.append(num)
for item in sorted(l):
    print(item.strftime('%d/%m/%Y'))
# Входные данные
# 5
# 2021-08-01
# 2021-08-02
# 2021-07-01
# 2021-06-01
# 2021-05-01

# Выходные данные
# 01/05/2021
# 01/06/2021
# 01/07/2021
# 01/08/2021
# 02/08/2021