str1, str2 = tuple(input().split())
str1 = list(str1)
str2 = list(str2)
str2[:2] = str1[:2]
str2 = ''.join(str2)
print(str2)