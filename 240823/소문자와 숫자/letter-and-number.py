string = input()
result = ''

for s in string:
    if s.isdigit():
        result+=s
        continue
    if s.isalpha():
        if ord('A')<=ord(s)<=ord('Z'):
            s = s.lower()
        result+=s
print(result)