n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    my_sum = 0
    for j in range(a, b+1):
        if j%2==0:
            my_sum+=j
    print(my_sum)