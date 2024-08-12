n = int(input())
num = 0
for i in range(n):
    arr = list(map(int, input().split()))
    if sum(arr)/4>60:
        print('pass')
        num += 1
    else:
        print('fail')
print(num)