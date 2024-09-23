class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight

n = int(input())

infos = []
for _ in range(n):
    n, h, w = input().split()
    infos.append(Info(n, h, w))

infos.sort(key=lambda x: x.h)

for info in infos:
    print(info.name, info.h, info.w, sep=' ')