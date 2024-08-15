n = int(input())
prices = list(map(int, input().split()))
mini = prices[0]
idx = -1
for i in range(n):
    if mini>prices[i]:
        mini = prices[i]
        idx = i

maxi = mini
for el in prices[idx:n]:
    if maxi<el:
        maxi=el
print(maxi-mini)