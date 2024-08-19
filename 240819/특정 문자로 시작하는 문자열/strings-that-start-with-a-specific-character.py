n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
alpha = input()

length = 0
cnt=0
for w in words:
    if w[0]==alpha:
        length+=len(w)
        cnt+=1
print(f'{cnt} {length/cnt:.2f}')