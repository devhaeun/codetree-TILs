n,m = map(int, input().split())
list_A = list(map(int, input().split()))

def sum_from_a1_to_a2(m):
    for _ in range(m):
        a1,a2 = map(int, input().split())
        my_sum = 0
        for i in range(a1-1, a2):
            my_sum+=list_A[i]
        print(my_sum)
sum_from_a1_to_a2(m)