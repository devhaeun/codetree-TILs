n = int(input())
for i in range(n):
    if i==0:
        for j in range(n):
            print('*', end=' ')
        print()
    else:
        for j in range(n):
            if j==n-1:
                print('*')
            elif j<i:
                print('*', end=' ')
            else:
                print(' ', end=' ')