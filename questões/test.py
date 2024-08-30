try:
    num1 = int(input("Digite um numero:"))
    num2 = int(input("Digite outro numero:"))
    resultado = num1 / num2

    print(f"O resultado da divisão é:{resultado}")
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except ValueError:
    print("Você deve digitar apenas numeros inteiros")