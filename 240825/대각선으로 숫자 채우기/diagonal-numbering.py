n,m = map(int, input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
cnt = 1

# 1행의 모든 열 채우기
for col in range(m):
    current_row = 0
    current_col = col

    while current_col>=0 and current_row<n:
        arr[current_row][current_col] = cnt

        current_row+=1
        current_col-=1
        cnt+=1

# 마지막 열 모두 채우기
for row in range(1, n):
    current_row = row
    current_col = m-1

    while current_col>=0 and current_row<n:
        arr[current_row][current_col] = cnt

        current_row+=1
        current_col-=1
        cnt+=1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()