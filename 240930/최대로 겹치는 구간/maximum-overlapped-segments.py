n = int(input())
offset = 100
arr = [0]*101

for _ in range(n):
    x1, x2 = map(int, input().split())
    if x1<0:
        x1+=offset
    if x2<0:
        x2+=offset
    for i in range(x1, x2):
        arr[i]+=1

print(max(arr))