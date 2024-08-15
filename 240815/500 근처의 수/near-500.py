arr = list(map(int, input().split()))
maxi = -1
mini = 1000
for el in arr:
    if el<500 and el>maxi:
        maxi = el
    elif el>500 and el<mini:
        mini = el
print(maxi, mini, sep=' ')