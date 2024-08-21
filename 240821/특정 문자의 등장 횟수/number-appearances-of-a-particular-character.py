string = input()
ee=0
eb=0
for i in range(len(string)-1):
    if string[i]=='e' and string[i+1]=='e':
        ee+=1
    if string[i]=='e' and string[i+1]=='b':
        eb+=1
print(ee, eb, sep=' ')