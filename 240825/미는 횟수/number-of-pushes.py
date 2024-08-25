A = input()
B = input()
n=-1

for i in range(len(A)):
    A = A[-1]+A[:-1]
    if A==B:
        n=i+1
        break
print(n)