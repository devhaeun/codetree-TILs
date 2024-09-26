a, b, c = map(int, input().split())

# 기준: 11월 1일 0시 0분
# 11월 11일 11시 11분 == ?분
start = 11 + 11*60 + 11*(24*60)

# 11월 a일 b시 c분 == ?분
end = c + b*60 + a*(24*60)

# 두 시간의 차를 구한다
time = end - start
if time<0:
    print(-1)
else:
    print(time)