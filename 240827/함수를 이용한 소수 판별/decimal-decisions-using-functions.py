a,b = map(int, input().split())

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

prime_sum = 0
for i in range(a,b+1):
    if is_prime(i):
        prime_sum += i
print(prime_sum)