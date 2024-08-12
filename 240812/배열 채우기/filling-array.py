numbers = list(map(int, input().split()))
arr = []
for num in numbers:
    if num==0:
        break
    arr.append(num)
for el in arr[::-1]:
    print(el, end=' ')