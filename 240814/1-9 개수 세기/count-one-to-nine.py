n = int(input())
arr = list(map(int, input().split()))
num = [0]*9
for el in arr:
    num[el-1]+=1
for i in range(9):
    print(num[i])