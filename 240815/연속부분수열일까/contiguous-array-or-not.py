n1, n2 = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
idxs = []
check=0

for i in range(len(arrA)):
    if arrB[0]==arrA[i]:
        idxs.append(i)
if len(idxs)!=0:
    for el in idxs:
        for j in range(len(arrB)):
            if arrA[el+j]==arrB[j]:
                check+=1
        if check==len(arrB):
            print('Yes')
            break
        check = 0
if check==0:
    print('No')