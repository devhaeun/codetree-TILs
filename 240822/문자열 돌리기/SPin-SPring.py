string = input()
print(string)
L = len(string)

for _ in range(L):
    string = string[-1]+string[:-1]
    print(string)