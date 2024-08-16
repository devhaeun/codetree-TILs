my_sum = 0
for i in range(4):
    my_sum+=sum(list(map(int, input().split()))[:i+1])
print(my_sum)