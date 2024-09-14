word1 = input()
word2 = input()

sorted1 = ''.join(sorted(word1))
sorted2 = ''.join(sorted(word2))
if sorted1 == sorted2:
    print('Yes')
else:
    print('No')