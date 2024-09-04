string_a = input()

def alpha_num(string):
    alphabet = []
    cnt = 0
    for s in string:
        if s not in alphabet:
            alphabet.append(s)
            cnt+=1
            if cnt>=2:
                print('Yes')
                return
    print('No')

alpha_num(string_a)