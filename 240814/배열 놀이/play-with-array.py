n,q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    lst = list(map(int, input().split()))
    if lst[0]==1:
        print(arr[lst[1]-1])
    elif lst[0]==2:
        idx=0
        if lst[1] in arr:
            idx = arr.index(lst[1])+1
        print(idx)
    else:
        for i in range(lst[1]-1, lst[2]):
            print(arr[i], end=' ')
        print()