class Student:
    def __init__(self, height, weight, number):
        self.h = height
        self.w = weight
        self.num = number
students = []

n = int(input())
for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))

students.sort(key=lambda x:(x.h, -x.w))

for student in students:
    print(student.h, student.w, student.num, sep=' ')