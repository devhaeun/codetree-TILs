n = int(input())
inputs = input().split()
inputs = ''.join(inputs)
for i in range(len(inputs)):
    if i!=0 and i%5==0:
        print()
    print(inputs[i], end='')