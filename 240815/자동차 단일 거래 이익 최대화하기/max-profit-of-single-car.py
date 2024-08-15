n = int(input())
prices = list(map(int, input().split()))
mini = min(prices[:n-1])
idx = prices.index(mini)
maxi = max(prices[idx+1:])

print(maxi-mini) if maxi>mini else print(0)