n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1

for col in range(n-1, -1, -1):
    if (n-col-1)%2==0:
        for row in range(n):
            arr[n-row-1][col]=cnt
            cnt+=1
    else:
        for row in range(n):
            arr[row][col]=cnt
            cnt+=1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()