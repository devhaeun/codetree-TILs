arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
arrSum = a+b+c
arrMean = arrSum//3
print(arrSum, arrMean, arrSum-arrMean, sep="\n")