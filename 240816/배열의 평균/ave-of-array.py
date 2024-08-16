my_list = []
row_mean = []
col_mean = []
total_mean = 0
for i in range(2):
    my_list.append(list(map(int, input().split())))
    temp_sum = sum(my_list[i])
    row_mean.append(temp_sum/4)
    total_mean+=temp_sum
for i in range(4):
    temp_sum = my_list[0][i] + my_list[1][i]
    col_mean.append(temp_sum/2)

for i in range(2):
    print('%.1f'%row_mean[i], end=' ')
print()
for i in range(4):
    print('%.1f'%col_mean[i], end=' ')
print()
total_mean/=8
print('%.1f'%total_mean)