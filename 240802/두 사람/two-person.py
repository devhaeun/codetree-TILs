x1 = input().split()
x1Age = int(x1[0])
x1Sex = x1[1]
x2 = input().split()
x2Age = int(x2[0])
x2Sex = x2[1]
if (x1Age>=19 and x1Sex=='M') or (x2Age>=19 and x2Sex=='M'):
    print(1)
else:
    print(0)