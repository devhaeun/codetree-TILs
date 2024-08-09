n = int(input())
a = ord('A')
for i in range(n):
    for j in range(n):
        if j<i:
            print(' ', end=' ')
        else:
            print(chr(a), end=' ')
            a+=1
            if a>ord('A')+25:
                a = ord('A')
    print()