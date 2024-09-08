n = int(input())
ints = list(map(int, input().split()))

def find_max(n):
    if n==0:
        return ints[0]
    return max(find_max(n-1), ints[n])

print(find_max(n-1))