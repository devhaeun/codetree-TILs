n = int(input())
arr = [0]*2001 # 위치 0 == arr[1000]
pos = 1000

for _ in range(n):
    x,D = input().split()
    x = int(x)
    arr[pos]+=1
    if D=='R':
        for i in range(1,x+1):
            pos+=1
            arr[pos]+=1
            # print(f'arr[{pos}]: {arr[pos]}')
    if D=='L':
        for i in range(1,x+1):
            pos-=1
            arr[pos]+=1
            # print(f'arr[{pos}]: {arr[pos]}')

# arr에서 0이 아닌 부분만 떼어오기
arr = [x for x in arr if x!=0]
# print(arr)

result = 0
for i in range(len(arr)-1):
    if arr[i]>=2 and arr[i+1]>=2:
        result+=1
print(result)