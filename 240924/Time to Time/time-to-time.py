a, b, c, d = map(int, input().split())

# a시 b분
time1 = a*60+b
# c시 d분
time2 = c*60+d

# 차
time = time2 - time1
print(time)