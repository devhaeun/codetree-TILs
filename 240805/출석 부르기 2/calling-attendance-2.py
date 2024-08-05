class_A = ['John', 'Tom', 'Paul', 'Sam']
while True:
    n = int(input())
    if n>4:
        print('Vacancy')
        break
    else:
        print(class_A[n-1])