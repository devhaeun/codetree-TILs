nums = list(map(int, input().split()))
sum = 0
num = 0
for el in nums:
    if el<250:
        sum+=el
        num+=1
    else:
        break
print(f"{sum} {sum/num:.1f}")