word1, word2 = tuple(input().split())
len1 = len(word1)
len2 = len(word2)

if len1>len2:
    print(word1, len1, sep=' ')
elif len2>len1:
    print(word2, len2, sep=' ')
else:
    print('same')