c,n = input().split()
n = int(n)
if c == 'A':
    for i in range(n):
        print(i+1, end=' ')
elif c == 'D':
    for i in range(n, 0, -1):
        print(i, end=' ')