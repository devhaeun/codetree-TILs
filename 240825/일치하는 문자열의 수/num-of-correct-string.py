n, A = tuple(input().split())
n = int(n)
cnt = 0

# n개의 문자열 주어질 때 문자열 A와 일치하는 것의 개수 세기
for _ in range(n):
    B = input()
    if A==B:
        cnt+=1
print(cnt)