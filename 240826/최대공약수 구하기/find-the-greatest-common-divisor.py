n,m = map(int, input().split())
def func(a,b):
    s = a if a<=b else b
    for i in range(s,0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
func(n,m)