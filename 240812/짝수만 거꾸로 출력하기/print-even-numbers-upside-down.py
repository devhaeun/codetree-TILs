n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
for el in arr[::-1]:
    if el%2==0:
        print(el, end=' ')