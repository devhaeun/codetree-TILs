start, end = map(int, input().split())
cnt = 0
for i in range(start, end):
    cnt2 = 0
    for j in range(1, i+1):
        if i%j==0:
            cnt2+=1
    if cnt2==3:
        cnt+=1
print(cnt)