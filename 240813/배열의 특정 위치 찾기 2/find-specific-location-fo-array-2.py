arr = list(map(int, input().split()))
odd = 0
even = 0
for i in range(10):
    if i%2==0:
        odd+=arr[i]
    else:
        even+=arr[i]
print(odd-even) if odd>=even else print(even-odd)