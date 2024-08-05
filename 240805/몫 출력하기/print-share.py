even = 0
while True:
    n = int(input())
    if n%2==0:
        print(n//2)
        even+=1
    if even==3:
        break