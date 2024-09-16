class Weather:
    def __init__(self, date, day, w):
        self.date = date
        self.day = day
        self.w = w

n = int(input())
temp = '2100-12-31'
for _ in range(n):
    date_, day_, w_ = tuple(input().split())
    weather1 = Weather(date_, day_, w_)
    if weather1.w == 'Rain' and weather1.date < temp:
        temp = weather1.date
        weather2 = Weather(weather1.date, weather1.day, weather1.w)

print(weather2.date, weather2.day, weather2.w, sep=' ')