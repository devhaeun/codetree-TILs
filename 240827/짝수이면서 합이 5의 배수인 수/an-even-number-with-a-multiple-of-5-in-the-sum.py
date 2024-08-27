n = int(input())

def yes_or_no(x):
    if x%2==0 and (x//10+x%10)%5==0:
        print('Yes')
    else:
        print('No')

yes_or_no(n)