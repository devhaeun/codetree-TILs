n = int(input())

def factorial(n):
    if n<=1:
        return 1
    return factorial(n-1)*n

result = factorial(n)
print(result)