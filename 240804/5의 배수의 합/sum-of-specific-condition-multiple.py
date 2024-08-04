a,b = map(int, input().split())
sum5 = 0
if a>b:
    n1=b
    n2=a
else:
    n1=a
    n2=b
for i in range(n1, n2+1):
    if i%5==0:
        sum5+=i
print(sum5)