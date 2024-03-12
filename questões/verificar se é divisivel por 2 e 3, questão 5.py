Num1 = int(input("Informe um valor:"))
Num2 = int(input("Informe outro valor:"))
Num3 = int(input("Informe mais um valor:"))
Num4 = int(input("Informe outro valor pfv:"))

Divisivel3 = bool
Divisivel2 = bool

if (Num1 or Num2 or Num3 or Num4) % 3 == 0:
    print(Num1, Num2, Num3, Num4, "São divisiveis por 3")
    
else:
    print("Não são divisiveis por 3")