n = int(input())
n_list = list(map(int, input().split()))

def func(lst):
    for i in range(len(lst)):
        if lst[i]<0:
            lst[i] = -lst[i]

func(n_list)
for el in n_list:
    print(el, end=' ')