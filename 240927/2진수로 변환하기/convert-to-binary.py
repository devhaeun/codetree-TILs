n = int(input())
remains = []

while n>=2:
    remains.append(n%2)
    n //= 2

n = str(n)
for i in range(len(remains)):
    n += str(remains[len(remains)-1-i])
print(n)