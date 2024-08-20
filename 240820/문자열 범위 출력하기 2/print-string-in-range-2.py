string = input()
n = int(input())

if n>len(string):
    for i in range(len(string)):
        print(string[len(string)-1-i], end='')
else:
    for i in range(n):
        print(string[len(string)-1-i], end='')