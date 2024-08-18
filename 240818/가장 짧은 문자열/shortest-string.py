w1 = input()
w2 = input()
w3 = input()

len1 = len(w1)
len2 = len(w2)
len3 = len(w3)

max_len = max(len1, len2, len3)
min_len = min(len1, len2, len3)
print(max_len-min_len)