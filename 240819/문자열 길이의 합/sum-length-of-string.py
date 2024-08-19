n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
length = 0
a_cnt = 0
for w in words:
    length+=len(w)
    if w[0]=='a':
        a_cnt+=1
print(length, a_cnt, sep=' ')