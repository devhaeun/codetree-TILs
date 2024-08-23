a,b = tuple(map(ord, input().split()))
sum_ab = a+b
sub_ab = a-b if a>b else b-a
print(sum_ab, sub_ab)