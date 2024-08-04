arr = []
for _ in range(10):
    temp = int(input())
    if temp>=0 and temp<=200:
        arr.append(temp)
sum_arr = sum(arr)
mean_arr = sum_arr/len(arr)
print(f"{sum_arr} {mean_arr:.1f}")