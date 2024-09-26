m1, d1, m2, d2 = map(int, input().split())
days_of_months = [31, 28, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]

def count_date(m, d):
    days = 0
    for i in range(m-1):
        days += days_of_months[i]
    return days+d

date1 = count_date(m1, d1)
date2 = count_date(m2, d2)
week_day = abs(date2 - date1)%7
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
if date1>=date2:
    print(weeks[-week_day])
else:
    print(weeks[week_day])