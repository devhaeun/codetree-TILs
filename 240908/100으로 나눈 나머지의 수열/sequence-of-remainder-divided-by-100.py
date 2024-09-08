n = int(input())

def find_value(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (find_value(n-1)*find_value(n-2))%100

print(find_value(n))