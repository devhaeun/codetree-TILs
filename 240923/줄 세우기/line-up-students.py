N = int(input())

infos = []
for i in range(N):
    h, w = map(int, input().split())
    infos.append((h, w, i+1))

infos.sort(key=lambda x: (-x[0], -x[1], x[2]))

for info in infos:
    print(info[0], info[1], info[2], sep=' ')