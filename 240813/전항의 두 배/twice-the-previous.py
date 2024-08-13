pp, p = map(int, input().split())
print(pp, p, sep=' ', end=' ')
for _ in range(8):
    pp, p = p, p+2*pp
    print(p, end=' ')