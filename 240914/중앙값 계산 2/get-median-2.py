n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = []

for i in range(n):
    sorted_numbers.append(numbers[i])
    sorted_numbers.sort()
    if i%2==0:
        print(sorted_numbers[len(sorted_numbers)//2], end=' ')