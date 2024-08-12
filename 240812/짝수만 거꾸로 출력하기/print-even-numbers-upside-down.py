n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
my_arr = []
for el in arr:
    if el%2==0:
        my_arr.append(el)
my_arr = my_arr[::-1]
for el in my_arr:
    print(el, end=' ')