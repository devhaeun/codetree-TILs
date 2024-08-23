string = input()
result = ''

for s in string:
    if ord('a')<=ord(s)<=ord('z'):
        result += s.upper()
    else:
        result += s.lower()
print(result)