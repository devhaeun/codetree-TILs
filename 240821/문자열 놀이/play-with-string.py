# 문자열 s, 질의의 수 q
s,q = tuple(input().split())
s = list(s)
q = int(q)

# q개의 질의
for _ in range(q):
    temp = input().split()
    a = temp[1]
    b = temp[2]
    if temp[0]=='1':
        # 1번 타입의 질의
        a = int(a)
        b = int(b)
        s[a-1],s[b-1] = s[b-1],s[a-1]
    elif temp[0]=='2':
        # 2번 타입의 질의
        for i in range(len(s)):
            if s[i]==a:
                s[i]=b
    result = ''.join(s)
    print(result)