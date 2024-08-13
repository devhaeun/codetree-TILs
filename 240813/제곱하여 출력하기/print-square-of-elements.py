n = int(input())
arr = list(map(int, input().split()))
new_arr = [el**2 for el in arr]
for el in new_arr:
    print(el, end=' ')