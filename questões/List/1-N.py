A = []

for i in range(0,20):
    A.append(float(input(f"insira o valor {i+1}° de graus celsius")))
print("primeiro valor:",A[0])
print("ultimo valor:",A[19])
print("media:",A / 10)