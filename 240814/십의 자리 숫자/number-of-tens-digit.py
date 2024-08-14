arr = list(map(int, input().split()))
nums = [0]*9
for el in arr:
    if el==0:
        break
    if el//10==0:
        pass
    else:
        nums[el//10-1]+=1
for i in range(9):
    print(f"{i+1} - {nums[i]}")