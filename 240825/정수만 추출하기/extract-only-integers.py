s1, s2 = tuple(input().split())
n1, n2 = '', ''
for s in s1:
    if ord('0')<=ord(s)<=ord('9'):
        n1+=s
    else:
        break
for s in s2:
    if ord('0')<=ord(s)<=ord('9'):
        n2+=s
    else:
        break
result = int(n1)+int(n2)
print(result)