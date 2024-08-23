alpha = ord(input())
if alpha==ord('z'):
    alpha = 'a'
else:
    alpha = chr(alpha+1)
print(alpha)