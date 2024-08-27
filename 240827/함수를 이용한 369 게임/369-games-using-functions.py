a,b = map(int, input().split())

def is_369(n):
    n = str(n)
    if '3' in n or '6' in n or '9' in n:
        return True

def is_three(n):
    return n%3==0 or is_369(n)

cnt=0
for i in range(a, b+1):
    if is_three(i):
        cnt+=1

print(cnt)