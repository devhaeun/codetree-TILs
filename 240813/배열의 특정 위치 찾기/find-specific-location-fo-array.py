arr = list(map(int, input().split()))
my_sum = 0
my_mean = 0
for el in arr[1::2]:
    my_sum+=el
for el in arr[2::3]:
    my_mean+=el
my_mean/=(len(arr)//3)
print(f"{my_sum} {my_mean:.1f}")