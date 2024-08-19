words = []
for _ in range(10):
    words.append(input())
alpha = input()
cnt=0
for el in words:
    if el[-1]==alpha:
        print(el)
        cnt+=1
if cnt==0:
    print('None')