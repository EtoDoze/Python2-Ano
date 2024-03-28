A = []
B = []

for i in range(0,10):
    A.append(int(input(f"Insira o valor {1+i}° de A:")))
    B.append(-(A[i]))
print("A:",A,"B:",B)