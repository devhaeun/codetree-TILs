m1 = input().split()
m2 = input().split()
m3 = input().split()

r1 = int(m1[0]=='Y' and int(m1[1])>=37)
r2 = int(m2[0]=='Y' and int(m2[1])>=37)
r3 = int(m3[0]=='Y' and int(m3[1])>=37)
result = r1+r2+r3
if result>=2:
    print('E')
else:
    print('N')