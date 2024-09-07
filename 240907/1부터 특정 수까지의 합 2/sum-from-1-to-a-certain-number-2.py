n = int(input())

def sum_to_n(n):
    if n==1:
        return 1
    previous = sum_to_n(n-1)
    result = previous + n
    return result

print(sum_to_n(n))