A = []
B = []

for i in range(0,15):
    A.append(int(input(f"insira o valor {i+1}° de A:")))
    B.append(A[i] ** 2)
    
print("Lista A:",A,"Lista B:",B)


