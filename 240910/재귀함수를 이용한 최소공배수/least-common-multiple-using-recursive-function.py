n = int(input())
numbers = list(map(int, input().split()))

# 최소공배수 구하는 재귀함수
def LCM(i):
    if i==0:
        result = 1
    else:
        result = LCM(i-1)

    if result==1:
        result*=numbers[i]
        
    elif result%numbers[i]!=0:
        if numbers[i] in [1,2,3,5,7]:
            result *= numbers[i]
        else:
            if numbers[i]%2==0:
                if result%4==0:
                    result*=2
                elif result%2==0:
                    result*=numbers[i]//2
                else:
                    result*=2
            else:
                result*=3 if result%3==0 else 9
    # print(f'{i}: {result}')
    return result

result = LCM(n-1)
print(result)