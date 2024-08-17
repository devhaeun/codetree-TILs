n = int(input())
prices = list(map(int, input().split()))
mini = prices[0]
max_gap=0

for price in prices:
    gap = price - mini
    if max_gap<gap:
        max_gap = gap
    if price<mini:
        mini = price
print(max_gap)