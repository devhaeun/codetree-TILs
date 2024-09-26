m1, d1, m2, d2 = map(int, input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def what_date(m, d):
    date = 0
    for i in range(m-1):
        date += days[i]
    return date+d

date1 = what_date(m1, d1)
date2 = what_date(m2, d2)

# 요일의 인덱스 찾기
A_idx = weeks.index(A)

# 날짜 사이에 n주+(gap%7)일의 간격이 있다면
gap = date2 - date1
n_weeks = gap//7
n_more_day = gap%7

# 요일의 인덱스가 gap%7보다 크면 n번
# gap%7보다 작으면 n+1번 등장
if A_idx>n_more_day:
    print(n_weeks)
else:
    print(n_weeks+1)