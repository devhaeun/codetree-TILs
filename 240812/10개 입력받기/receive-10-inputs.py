nums = list(map(int, input().split()))
new_nums = []
for num in nums:
    if num==0:
        break
    new_nums.append(num)
new_sum = sum(new_nums)
print(f"{new_sum} {new_sum/len(new_nums):.1f}")