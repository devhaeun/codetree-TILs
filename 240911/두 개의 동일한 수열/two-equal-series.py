n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort()
arr_B.sort()
is_same = True
for i in range(n):
    if arr_A[i]!=arr_B[i]:
        is_same = False

if is_same:
    print('Yes')
else:
    print('No')