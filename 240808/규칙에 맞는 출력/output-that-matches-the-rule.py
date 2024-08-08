n = int(input())
for i in range(n):
    temp = n-i
    for j in range(i+1):
        print(temp, end=' ')
        temp+=1
    print()