N, B = map(int, input().split())
nums = []

while N>=B:
    temp = N % B
    nums.append(temp)
    N //= B

result = str(N)
for i in range(len(nums)):
    result += str(nums[len(nums)-1-i])

print(result)