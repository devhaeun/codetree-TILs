n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
max_sum = 0
for i in range(n):
    temp_sum = numbers[i]+numbers[2*n-i-1]
    if max_sum<temp_sum:
        max_sum = temp_sum
print(max_sum)