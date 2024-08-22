A = input()
q = input()
L = q.count('L')
R = q.count('R')
if L>R:
    left = L-R
    # 왼쪽으로 left 만큼 밀기
    for _ in range(left):
        A = A[1:]+A[0]
elif R>L:
    right = R-L
    # 오른쪽으로 right 만큼 밀기
    for _ in range(right):
        A = A[-1]+A[:-1]

print(A)