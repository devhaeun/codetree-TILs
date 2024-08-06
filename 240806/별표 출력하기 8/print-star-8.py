n = int(input())
for i in range(n):
    if (i+1)%2==1:
        print('*', end='')
    else:
        for j in range(i+1):
            print('*', end=' ')
    print()