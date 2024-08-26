def square(r,c):
    for _ in range(r):
        for _ in range(c):
            print(1, end='')
        print()
n, m = map(int, input().split())
square(n,m)