a,o,c = input().split()
a = int(a)
c = int(c)

def add(n1, n2):
    result = n1+n2
    print(f"{n1} + {n2} = {result}")

def sub(n1, n2):
    result = n1-n2
    print(f"{n1} - {n2} = {result}")

def pro(n1, n2):
    result = n1*n2
    print(f"{n1} * {n2} = {result}")

def div(n1, n2):
    result = n1//n2
    print(f"{n1} / {n2} = {result}")

if o == '+':
    add(a,c)
elif o=='-':
    sub(a,c)
elif o=='*':
    pro(a,c)
elif o=='/':
    div(a,c)
else:
    print('False')