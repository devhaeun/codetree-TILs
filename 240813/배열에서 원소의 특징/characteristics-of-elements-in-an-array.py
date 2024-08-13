arr = list(map(int, input().split()))
new_arr = []
for el in arr:
    if el%3==0:
        break
    new_arr.append(el)
print(new_arr[-1])