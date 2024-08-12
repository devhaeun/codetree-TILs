grades = list(map(float, input().split()))
gr_mean = sum(grades)/len(grades)
print('%.1f'%gr_mean)