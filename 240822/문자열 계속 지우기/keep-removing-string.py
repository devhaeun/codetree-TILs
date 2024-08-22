A = input()
B = input()

while B in A:
    idx = A.find(B)
    A_list = list(A)
    for i in range(len(B)):
        A_list.pop(idx)
    A = ''.join(A_list)
print(A)