n = int(input())
arr = list(map(int, input().split()))
mini = arr[0]
for el in arr:
    if mini>el:
        mini = el
print(mini, arr.count(mini), sep=' ')