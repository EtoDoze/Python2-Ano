A = []
B = []
C = []

for i in range(0, 20):
    A.append(int(input(f"insira o {i + 1}° de A:")))
    B.append(int(input(f"insira o {i + 1}° de B:")))
    C.append(A[i] - B[i])
    
print("Lista A:",A,"Lista B:",B,"Lista C:",C)