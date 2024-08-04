n = int(input())
cnt=1
while n>1:
    n//=cnt
    cnt+=1
print(cnt-1)