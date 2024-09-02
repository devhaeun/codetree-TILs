n1,n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 함수
def consecutive(l1, l2):
    check = False
    for i in range(len(l1)-len(l2)+1):
        if l1[i] == l2[0]:
            for j in range(1, len(l2)):
                if l1[i+j] == l2[j]:
                    check = True
                else:
                    check = False
                    break
            if check:
                return(True)
    return(False)

if consecutive(A, B):
    print('Yes')
else:
    print('No')