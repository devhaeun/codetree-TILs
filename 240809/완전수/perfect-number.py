start, end = map(int, input().split())
cnt = 0
for i in range(start, end+1):
    my_sum = 0
    for j in range(1, i):
        if i%j==0:
            my_sum+=j
    if my_sum == i:
        cnt+=1
print(cnt)