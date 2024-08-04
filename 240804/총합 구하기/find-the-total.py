a,b = map(int, input().split())
my_sum = 0
for i in range(a,b+1):
    if i%6==0 and i%8!=0:
        my_sum+=i
print(my_sum)