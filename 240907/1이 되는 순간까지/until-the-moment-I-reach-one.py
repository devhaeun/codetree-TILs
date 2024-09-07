n = int(input())
cnt = 0

def func(n, cnt):
    if n==1:
        print(cnt)
        return
    cnt+=1
    if n%2==0:
        func(n//2, cnt)
    else:
        func(n//3, cnt)

func(n, cnt)