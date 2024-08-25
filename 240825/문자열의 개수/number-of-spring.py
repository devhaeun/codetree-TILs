odd = []
cnt = 0

while True:
    word = input()
    if word == '0':
        break
    cnt+=1
    if cnt%2==1:
        odd.append(word)

print(cnt)
for el in odd:
    print(el)