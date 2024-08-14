scores = list(map(int, input().split()))
cntlst = [0]*10
for s in scores:
    if s==0:
        break
    if s//10==0:
        pass
    cntlst[s//10-1]+=1
for i in range(9, -1, -1):
    print(f"{(i+1)*10} - {cntlst[i]}")