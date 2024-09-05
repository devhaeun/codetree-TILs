n,m = map(int, input().split())
a = list(map(int, input().split()))

def func(m):
    result = 0
    while m>1:
        result += a[m-1]
        if m%2==1:
            m-=1
        else:
            m//=2
    print(result)

func(m)