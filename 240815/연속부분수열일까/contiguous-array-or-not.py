n1, n2 = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

check=True
cnts = []

for i in range(len(arrB)):
    cnts.append(arrA.count(arrB[i]))
    if cnts[i]==0:
        check=False

if check:
    for i in range(len(arrA)):
        if arrA[i]==arrB[0]:
            found = True
            for j in range(1,len(arrB)):
                if arrA[i+j]!=arrB[j]:
                    found=False
                    break
            if found:
                print('Yes')
                break
    if not found:
        check = False
if not check:
    print('No')