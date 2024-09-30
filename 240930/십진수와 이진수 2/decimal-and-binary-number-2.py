N = input()

# 이진수 -> 십진수
result = 0
for i in range(len(N)):
    result = result*2 + int(N[i])

result *= 17

# 십진수 -> 이진수
nums = []
while result>=2:
    nums.append(result%2)
    result //= 2

result = str(result)
for i in range(len(nums)):
    result += str(nums[len(nums)-1-i])

print(result)