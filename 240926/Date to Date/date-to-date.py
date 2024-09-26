m1, d1, m2, d2 = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_date(m, d):
    date = 0
    for i in range(m-1):
        date += days[i]
    return date+d

date1 = count_date(m1, d1)
date2 = count_date(m2, d2)
print(date2-date1+1)