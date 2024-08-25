# 입력되는 수의 개수 n
n = int(input())

# n개의 수가 주어질 때 모든 수를 더하기
sum_ = 0
for _ in range(n):
    num = int(input())
    sum_ += num

# 모든 수를 더한 값을 좌측으로 한 칸 민 결과 출력
sum_ = str(sum_)
result = sum_[1:]+sum_[0]
print(result)