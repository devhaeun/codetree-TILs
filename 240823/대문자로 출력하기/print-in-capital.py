string = input()
result = ''
for s in string:
    if s.isalpha():
        if ord('a')<=ord(s)<=ord('z'):
            s = s.upper()
        result += s.upper()
print(result)