a,b = map(int, input().split())
print(f"{a//b}.", end='')
for i in range(20):
    num = a%b*10
    new = num//b
    a = num-b*new*10
    print(new, end='')