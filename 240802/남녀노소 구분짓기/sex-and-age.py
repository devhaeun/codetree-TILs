sex = int(input()) # 남자 0 여자 1
age = int(input())
if sex==0:
    if age>=19:
        print('MAN')
    else:
        print('BOY')
else:
    if age>=19:
        print('WOMAN')
    else:
        print('GIRL')