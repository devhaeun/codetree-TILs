n = int(input())

def sqrsum(n):
    if n<10:
        return n**2
    return sqrsum(n//10) + (n%10)**2

print(sqrsum(n))