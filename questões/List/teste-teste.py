A = []
B = []

for i in range(0.25):
    A.append(float(input(f"Insira a temperatura {i+1}° de graus celsius")))
    B.append((A[i] * 1.8) + 32)
print("C°:",A,"F°:",B)