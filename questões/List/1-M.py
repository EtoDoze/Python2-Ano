A = []

for i in range(0,10):
    
    valor = int(input("Qual operação queres fazer? (adição/subtração/divisão/multiplicação)"))

    if valor == "adição":
        soma1 = int(input("Qual valor a ser somado?:"))
        soma2 = int(input("Qual o outro valor a ser somado?:"))
    
        soma = soma1 + soma2
        A.append(A[i] == soma)
        
    elif valor == "subtração":
        sub1 = int(input("Qual valor a ser subtração?:"))
        sub2 = int(input("Qual o outro valor a ser subtração?:"))
    
        sub = sub1 - sub2
        A.append(A[i] == sub)
        
    if valor == "multiplicação":
        multi1 = int(input("Qual valor a ser multiplicação?:"))
        multi2 = int(input("Qual o outro valor a ser multiplicação?:"))
    
        multi = multi1 * multi2
        A.append(A[i] == multi)
        
    if valor == "divisão":
        div1 = int(input("Qual valor da divisão?:"))
        div2 = int(input("Qual o outro valor a ser dividido?:"))
    
        div = div1 * div2
        A.append(A[i] == div)
        
print(A)