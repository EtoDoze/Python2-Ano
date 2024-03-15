B = int(input("Qual numero você quer elevar?:"))
E = int(input("Qual o expoente?:"))
Valor = B ** E

while True:
    
    if ((B ** E) == Valor) and ((Valor or B or E) > 0):
        print(Valor)
        break
    elif (B or E or Valor) <= 0:
        print("expoente ou base invalidos, use numeros positivos")
        break