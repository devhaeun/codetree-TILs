arr = list(map(int, input().split()))
new_arr = []
for el in arr:
    if el==0:
        break
    new_arr.append(el)
my_sum = new_arr[-1]+new_arr[-2]+new_arr[-3]
print(my_sum)