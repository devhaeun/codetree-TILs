n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (arr[i], i+1)

arr.sort(key=lambda x:x[0])
for i in range(n):
    arr[i] = (arr[i][0], arr[i][1], i+1)

arr.sort(key=lambda x:x[1])
for i in range(n):
    print(arr[i][2], end=' ')