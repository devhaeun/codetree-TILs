nums = list(map(int, input().split()))
evens = []
for num in nums:
    if num == 0:
        break
    if num%2==0:
        evens.append(num)
print(f"{len(evens)} {sum(evens)}")