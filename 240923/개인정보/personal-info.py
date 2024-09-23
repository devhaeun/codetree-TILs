class Info:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
infos = []

for _ in range(5):
    n, h, w = input().split()
    h = int(h)
    w = float(w)
    infos.append(Info(n, h, w))

infos.sort(key=lambda x: x.name)
print('name')
for info in infos:
    print(info.name, info.h, info.w, sep=' ')
print()

infos.sort(key=lambda x: -x.h)
print('height')
for info in infos:
    print(info.name, info.h, info.w, sep=' ')