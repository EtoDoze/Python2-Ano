num1 = 1
num2 = 1
num3 = 0

lista = [0,1,1]

def fibo(numero):
    for i in range(0, 10):
        num2 = lista[-1]
        num1 = lista[-2]
        num3 = num2 + num1
        lista.append(num3)
        print(f"o numero {i}° da sequencia é:{lista}")
    print(f"O elemento {numero}° da sequenci a fibonnaci é: {lista[numero -1]}")

numeroa = int(input("Insira o termo que queres achar da sequencia fibonnaci:"))
fibo(numeroa)
