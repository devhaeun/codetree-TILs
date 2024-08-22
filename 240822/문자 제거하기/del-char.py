word = list(input())
while len(word)>1:
    n = int(input())
    word.pop(n) if n<len(word) else word.pop(-1)
    result = ''.join(word)
    print(result)