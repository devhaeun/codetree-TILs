a,b = list(map(int, input().split()))
cntlst = [0]*10
while a>0:
    cntlst[a%b]+=1
    a//=b
my_sum=0
for n in cntlst:
    my_sum+=n**2
print(my_sum)