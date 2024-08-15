n = int(input())
nums = list(map(int, input().split()))
gap = 100
for i in range(n-1):
    temp = nums[i+1]-nums[i]
    if gap>temp:
        gap = temp
print(gap)