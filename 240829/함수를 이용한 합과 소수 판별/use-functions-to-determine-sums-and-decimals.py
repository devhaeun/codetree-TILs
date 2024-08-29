a,b = map(int, input().split())
cnt=0

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_sum_even(n):
    if n<10 and n%2==0:
        return True
    elif n<100:
        result = n%10 + n//10
        if result%2==0:
            return True
    else:
        return False

for i in range(a,b+1):
    if is_prime(i) and is_sum_even(i):
        cnt+=1
print(cnt)