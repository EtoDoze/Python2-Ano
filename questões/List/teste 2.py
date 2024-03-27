A = []
soma = 0

for i in range(0,5):
    A.append(int(input("insira um valor:")))
    if A[i] % 2 != 0:
        soma = soma + A[i]
print("soma dos impares é:", soma)