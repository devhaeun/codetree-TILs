string = input()
even = ''
for i in range(len(string)):
    if i%2!=0:
        even+=string[i]
for i in range(len(even)-1,-1,-1):
    print(even[i], end='')