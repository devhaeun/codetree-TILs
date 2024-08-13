n = int(input())
cnt=0
for i in range(1,11):
    print(n*i, end=' ')
    if n*i%5==0:
        cnt+=1
    if cnt==2:
        break