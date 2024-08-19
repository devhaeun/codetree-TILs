arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']
cnt = 0
alpha = input()
for i in range(5):
    if arr[i][2]==alpha:
        print(arr[i])
        cnt+=1
    if arr[i][3]==alpha:
        print(arr[i])
        cnt+=1
print(cnt)