n = int(input())

def func(n):
    if n<=2:
        return n
    return func(n-2)+n

result = func(n)
print(result)