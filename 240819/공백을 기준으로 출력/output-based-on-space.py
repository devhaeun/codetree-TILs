str1 = input()
str2 = input()
string = str1+str2
result = ''
for i in range(len(string)):
    if string[i]!=' ':
        result+=string[i]
print(result)