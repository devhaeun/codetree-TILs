for _ in range(5):
    my_list = list(input().split())
    for i in range(3):
        my_list[i] = chr(ord(my_list[i])-32)
        print(my_list[i], end=' ')
    print()