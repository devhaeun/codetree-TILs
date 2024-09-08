n = int(input())

def repeat_cnt(n):
    if n==2:
        return 1
    if n%2==0:
        temp = repeat_cnt(n//2)
    else:
        temp = repeat_cnt(n*3+1)
    return temp + 1

print(repeat_cnt(n))