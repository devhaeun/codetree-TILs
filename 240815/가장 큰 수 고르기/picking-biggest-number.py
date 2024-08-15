arr = list(map(int, input().split()))
maxi = arr[0]
for el in arr:
    if maxi<el:
        maxi = el
print(maxi)