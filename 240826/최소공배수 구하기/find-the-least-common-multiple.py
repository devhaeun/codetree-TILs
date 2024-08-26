n,m = map(int, input().split())
def min_mul(n,m):
    result = 1
    d = 2
    while True:
        if n%d==0 and m%d==0:
            n//=d
            m//=d
            result*=d
        else:
            d+=1
        
        if d>n or d>m:
            result = result*n*m
            break
    print(result)
min_mul(n,m)