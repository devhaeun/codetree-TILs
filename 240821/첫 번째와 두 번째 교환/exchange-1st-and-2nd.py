string = list(input())
first = string[0]
second = string[1]
for i in range(len(string)):
    if string[i]==first:
        string[i] = second
        continue
    elif string[i]==second:
        string[i] = first
        continue
string = ''.join(string)
print(string)