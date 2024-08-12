n = int(input())
grades = list(map(float, input().split()))
gr_mean = sum(grades)/n
print('%.1f'%gr_mean)
if gr_mean>=4.0:
    print('Perfect')
elif gr_mean>=3.0:
    print('Good')
else:
    print('Poor')