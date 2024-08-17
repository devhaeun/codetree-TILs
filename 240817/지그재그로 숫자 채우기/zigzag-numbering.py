n,m = map(int, input().split())
cnt=0
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for col in range(m):
    for row in range(n):
        if col%2==0:
            arr[row][col] = cnt
        else:
            arr[n-row-1][col] = cnt
        cnt+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()