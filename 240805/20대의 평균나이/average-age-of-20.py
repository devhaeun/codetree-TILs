sum_age = 0
cnt = 0
while True:
    age = int(input())
    if age//10!=2:
        break
    sum_age+=age
    cnt+=1
print('%.2f'%(sum_age/cnt))