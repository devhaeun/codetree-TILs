class Person:
    def __init__(self, name, dst, loc):
        self.name = name
        self.dst = dst
        self.loc = loc

n = int(input())
temp = 'a'
for _ in range(n):
    p_name, p_dst, p_loc = tuple(input().split())
    person1 = Person(p_name, p_dst, p_loc)
    if person1.name > temp:
        temp = person1.name[0]
        person2 = person1

print(f'name {person2.name}')
print(f'addr {person2.dst}')
print(f'city {person2.loc}')