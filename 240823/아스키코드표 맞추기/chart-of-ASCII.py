codes = list(map(int, input().split()))
for i in range(len(codes)):
    codes[i] = chr(codes[i])
    print(codes[i], end=' ')