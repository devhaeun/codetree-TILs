A = input()
q = input()
L = q.count('L')
R = q.count('R')
if L>R:
    left = L-R
    # 왼쪽으로 left 만큼 밀기
    A = A[left:]+A[:left]
elif R>L:
    right = R-L
    # 오른쪽으로 right 만큼 밀기
    A = A[-1*right:]+A[:-1*right]

print(A)