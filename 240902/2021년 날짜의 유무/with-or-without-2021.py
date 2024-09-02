M,D = map(int, input().split())

# 함수
def is_in_2021(m, d):
    if m==2 and d<29:
        return True
    elif m in [1, 3, 5, 7, 8, 10, 12] and d<32:
        return True
    elif m in [4, 6, 9, 11] and d<31:
        return True
    else:
        return False

if is_in_2021(M, D):
    print('Yes')
else:
    print('No')