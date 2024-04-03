A = []
B = []

cont = 0

while cont <= 11:
    A.append(int(input(f"Insira o valor {cont + 1}° de A:")))
    
    if not (A[cont] % 2) == 0:
        B.append(A[cont] * 2)
    else:
        B.append(A[cont])

    cont = cont + 1

print("A:",A,"B:",B) 