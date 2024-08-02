arr = input().split()
a = int(arr[0])
b = int(arr[1])
first = 1 if a<b else 0
second = 1 if a==b else 0
print(f"{first} {second}")