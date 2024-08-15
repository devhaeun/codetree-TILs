n = int(input())
arr = list(map(int, input().split()))
idx = n
maxi = -1

while idx>0:
    for i in range(idx):
        if maxi<arr[i]:
            maxi = arr[i]
    idx = arr.index(maxi)
    print(idx+1, end=' ')
    maxi = -1