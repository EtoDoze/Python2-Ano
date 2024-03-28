A = []
B = []

for i in range(0,10):
    A.append(int(input(f"Insira um valor {i+1}° para A:")))
    B.append(A[i] / 2)
print("A:",A,"B:",B)