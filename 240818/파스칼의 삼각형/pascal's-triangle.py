n = int(input())
arr = [
    [0 for _ in range(i+1)]
    for i in range(n)
]

for i in range(n):
    for j in range(i+1):
        if j==0 or j==i:
            arr[i][j] = 1
            continue
        arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()