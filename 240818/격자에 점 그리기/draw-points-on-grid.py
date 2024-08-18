n,m = tuple(map(int, input().split()))
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1
for _ in range(m):
    r,c = tuple(map(int, input().split()))
    grid[r-1][c-1] = cnt
    cnt+=1
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()