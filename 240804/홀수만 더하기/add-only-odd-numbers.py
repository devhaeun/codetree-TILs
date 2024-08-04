n = int(input())
my_sum = 0
for _ in range(n):
    temp = int(input())
    if temp%2==1 and temp%3==0:
        my_sum+=temp
print(my_sum)