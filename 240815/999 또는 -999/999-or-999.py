arr = list(map(int, input().split()))
maxi = arr[0]
mini = arr[0]
for el in arr:
    if el==999 or el==-999:
        break
    if maxi<el:
        maxi = el
    if mini>el:
        mini = el
print(maxi, mini, sep=' ')