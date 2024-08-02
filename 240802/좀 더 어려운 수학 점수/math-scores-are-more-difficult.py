A = input().split()
Amath = int(A[0])
Aeng = int(A[1])
B = input().split()
Bmath = int(B[0])
Beng = int(B[1])
if Amath>Bmath:
    print('A')
elif Amath<Bmath:
    print('B')
else:
    print('A') if Aeng>Beng else print('B')