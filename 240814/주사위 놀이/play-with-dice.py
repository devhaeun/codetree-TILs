dice = list(map(int, input().split()))
num = [0]*6
for x in dice:
    num[x-1]+=1
for i in range(6):
    print(f"{i+1} - {num[i]}")