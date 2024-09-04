string_a = input()

def alpha_num(string):
    cnt = 0
    for s in string:
        if string.count(s)>=2:
            cnt+=1
            if cnt>=2:
                print('Yes')
                return
    print('No')
alpha_num(string_a)