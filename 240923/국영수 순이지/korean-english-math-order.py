n = int(input())

scores = []
for _ in range(n):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    scores.append((name, kor, eng, math))

scores.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for score in scores:
    print(score[0], score[1], score[2], score[3], sep=' ')