n,m = map(int, input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

arr[0][0] = 1
row = 0
col = 1
cnt=2
while True:
    arr[row][col] = cnt
    if row==n-1 and col==m-1:
        break
    cnt+=1
    row+=1
    col-=1
    if col<0 or row>n-1:
        if arr[0][m-1]:
            row = row+col+1-(m-1)
            col = m-1
        else:
            col = row+col+1
            row = 0

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()