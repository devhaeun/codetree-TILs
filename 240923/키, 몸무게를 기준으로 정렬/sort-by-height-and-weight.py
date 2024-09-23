n = int(input())

infos = []
for _ in range(n):
    n, h, w = input().split()
    h = int(h)
    w = int(w)
    infos.append((n, h, w))

infos.sort(key=lambda x: (x[1], -x[2]))
for info in infos:
    print(info[0], info[1], info[2], sep=' ')