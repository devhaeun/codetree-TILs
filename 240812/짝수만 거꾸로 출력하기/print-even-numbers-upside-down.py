n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
arr = arr[::-1]
for el in arr:
    if el%2==0:
        print(el, end=' ')