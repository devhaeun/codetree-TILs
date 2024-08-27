n = int(input())
def func(n):
    my_sum = 0
    for i in range(1, n+1):
        my_sum += i
    my_sum//=10
    return(my_sum)
result = func(n)
print(result)