a, b = map(int, input().split())
n = input()

# a진수 -> 십진수
result = 0
for i in range(len(n)):
    result = result*a + int(n[i])

# 십진수 -> b진수
nums = []
while result >= b:
    nums.append(result%b)
    result//=b

result = str(result)
for i in range(len(nums)):
    result += str(nums[len(nums)-1-i])

print(result)