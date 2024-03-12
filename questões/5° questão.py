Num1 = int(input("Informe um valor:"))
Num2 = int(input("Informe outro valor"))
Num3 = int(input("Informe outro valor"))
Num4 = int(input("Informe outro valor"))

soma = Num1 + Num2 + Num3 + Num4
#Divisivel por 3 e 2 num1

if (soma % 3 == 0) and (soma % 2 != 0):
    print(soma, "é divisivel por 3")

elif (soma % 3 != 0) and (soma % 2 == 0):
     print(soma, "é divisivel por 2")
     
elif (soma % 3 == 0) and (soma % 2 == 0):
    print(soma, "é divisivel por 2 e 3")
 
else: 
    print(soma, "não é divisivel por 3, nem por 2")


