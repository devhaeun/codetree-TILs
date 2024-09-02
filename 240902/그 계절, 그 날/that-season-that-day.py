Y, M, D = map(int, input().split())

# 윤년인지 확인하는 함수
def leap_year(y):
    if y%4==0:
        if y%100==0 and y%400!=0:
            return False
        else:
            return True
    return False

# 특정 날짜 존재 여부 확인 함수 (tf: 윤년 여부)
def calendar(m, d, tf):
    if m==2:
        if tf and d<30 or not tf and d<29:
            return True
    elif m in [1, 3, 5, 7, 8, 10, 12] and d<32:
        return True
    elif m in [4, 6, 9, 11] and d<31:
        return True
    return False

# 계절 출력 함수
def season(y, m, d):
    # M월 D일 존재 여부 확인
    tf = leap_year(y)
    if calendar(m, d, tf):
        # 계절 출력
        if 3<=m<6:
            print('Spring')
        elif 6<=m<9:
            print('Summer')
        elif 9<=m<12:
            print('Fall')
        else:
            print('Winter')
    else:
        # -1 출력
        print(-1)

season(Y, M, D)