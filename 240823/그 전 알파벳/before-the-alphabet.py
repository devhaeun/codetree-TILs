alpha = ord(input())

if alpha==ord('a'):
    alpha = 'z'
else:
    alpha = chr(alpha-1)
print(alpha)