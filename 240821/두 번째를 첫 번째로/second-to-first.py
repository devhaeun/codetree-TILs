word = list(input())
first = word[0]
second = word[1]
for i in range(len(word)):
    if word[i]==second:
        word[i]=first
word = ''.join(word)
print(word)