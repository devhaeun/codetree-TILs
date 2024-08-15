n = int(input())
arr = list(map(int, input().split()))
arr.sort()
maxi = -1
for el in arr[n::-1]:
    if arr.count(el)==1:
        maxi = el
        break
print(maxi)