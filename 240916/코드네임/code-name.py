class Info:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

lowest = Info('_', 100)
for _ in range(5):
    name, score = input().split()
    info = Info(name, score)
    if info.score<=lowest.score:
        lowest = info
print(lowest.name, lowest.score, sep=' ')