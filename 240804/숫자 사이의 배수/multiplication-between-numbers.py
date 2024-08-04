a,b = map(int, input().split())
my_sum = 0
cnt=0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        my_sum+=i
        cnt+=1
print(f"{my_sum} {my_sum/cnt:.1f}")