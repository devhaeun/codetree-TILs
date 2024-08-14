cntlst = [0]*4
for i in range(3):
    p = list(input().split())
    p[1] = int(p[1])
    if p[1]>=37:
        if p[0]=='Y':
            cntlst[0]+=1
        else:
            cntlst[1]+=1
    elif p[0]=='Y':
        cntlst[2]+=1
    else:
        cntlst[3]+=1
for i in range(4):
    print(cntlst[i], end=' ')
if cntlst[0]>=2:
    print('E')