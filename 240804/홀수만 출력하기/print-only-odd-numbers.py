n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    if temp%2==1 and temp%3==0:
        arr.append(temp)
for j in range(len(arr)):
    print(arr[j])