A = []
B = []
soma = 0
multi = 0

for i in range(0,1):
    A.append(int(input(f"Insira o valor {i+1}° de A:")))
    soma = A[i] - 1
    for cont in range(0,A[i]):
        soma = cont 
        multi = soma + cont
        print(cont, soma)
    B.append(multi)

print("A:",A,"B:",B)