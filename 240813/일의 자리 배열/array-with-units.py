arr = list(map(int, input().split()))
for i in range(2, 10):
    temp = (arr[i-2]+arr[i-1])%10
    arr.append(temp)
for el in arr:
    print(el, end=' ')