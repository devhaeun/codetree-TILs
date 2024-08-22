word, q = tuple(input().split())
q = int(q)

# q번의 요청 수행
for _ in range(q):
    n = int(input())
    if n==1:
        # 1번 요청
        word = word[1:]+word[0]
    elif n==2:
        # 2번 요청
        word = word[-1]+word[:-1]
    elif n==3:
        # 3번 요청
        word = word[-1::-1]
    print(word)