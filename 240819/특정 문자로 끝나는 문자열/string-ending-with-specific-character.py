words = []
for _ in range(10):
    words.append(input())
alpha = input()
for el in words:
    if el[-1]==alpha:
        print(el)