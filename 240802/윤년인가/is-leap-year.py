y = int(input())
if y%4==0 and not(y%100==0 and y%400!=0):
    print('true')
else:
    print('false')