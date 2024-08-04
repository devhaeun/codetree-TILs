n = int(input())
my_sum = 0
for i in range(1, 101):
    my_sum+=i
    if my_sum>=n:
        print(i)
        break