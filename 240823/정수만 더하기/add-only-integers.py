A = input()
sumA = 0

for x in A:
    if x.isdigit():
        sumA += int(x)
print(sumA)