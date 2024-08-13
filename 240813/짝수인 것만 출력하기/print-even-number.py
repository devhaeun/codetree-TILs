n = int(input())
arr = list(map(int, input().split()))
new_arr = [el for el in arr if el%2==0]
for el in new_arr:
    print(el, end=' ')