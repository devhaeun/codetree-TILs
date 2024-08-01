inputs = input().split()
h = int(inputs[0])
w = int(inputs[1])
b = int(w/(h/100)**2)
print(b)
if b>=25:
    print("Obesity")