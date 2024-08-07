n = int(input())
for i in range(n-n%2 or 1):
    if i==0:
        for j in range(n):
            print('*', end=' ')
        print()
    else:
        for j in range(n):
            if j%2==1 and j>=i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()