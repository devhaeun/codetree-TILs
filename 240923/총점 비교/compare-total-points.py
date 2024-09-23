class Score:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
scores = []

n = int(input())
for _ in range(n):
    n, s1, s2, s3 = input().split()
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    scores.append(Score(n, s1, s2, s3))

scores.sort(key=lambda x: x.s1 + x.s2 + x.s3)

for score in scores:
    print(score.name, score.s1, score.s2, score.s3, sep=' ')