n = int(input())
arr = [1, n]
for i in range(2, 100):
    temp = arr[i-2]+arr[i-1]
    arr.append(temp)
    if temp>100:
        break
for el in arr:
    print(el, end=' ')