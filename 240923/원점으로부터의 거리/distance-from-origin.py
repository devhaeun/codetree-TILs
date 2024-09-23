class Point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.n = number
points = []

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    points.append(Point(x, y, i+1))

points.sort(key=lambda x: abs(x.x)+abs(x.y))
for point in points:
    print(point.n)