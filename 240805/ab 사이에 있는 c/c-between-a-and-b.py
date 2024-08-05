a,b,c = map(int, input().split())
satisfied = False
while a<=b:
    if a%c==0:
        satisfied=True
        break
    a+=1
if satisfied:
    print('YES')
else:
    print('NO')