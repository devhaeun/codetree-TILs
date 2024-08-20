A = input()
abc = []
cnt = 0
result = ''

for el in A:
    if not el in abc:
        if cnt==0:
            abc.append(el)
            cnt+=1
        else:
            result += abc[0]+str(cnt)
            abc.pop()
            abc.append(el)
            cnt=1
    else:
        cnt+=1
result += abc[0]+str(cnt)
print(len(result))
print(result)