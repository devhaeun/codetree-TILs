n = int(input())
n_list = list(map(int, input().split()))

def divide_even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]//=2

divide_even(n_list)
for el in n_list:
    print(el, end=' ')