import Dados as Contas

Contas.linha(100)
print("INFO BANK")
Contas.linha(100)

cadastro = str(input("Bem vindo, você ainda não está cadastrado. Deseja realizar o cadastro? S/N:")).lower()
while True:
    if cadastro not in ['sim', 's']:
        print("Você precisa continuar para realizar o cadastro")
        cadastro = str(input("Deseja realizar o cadastro? S/N:")).lower()

    else:
        print("Otimo")
        break

print("Certo, proximo passo")

Nome = str(input("Insira seu nome:"))
cpf_user = str(input("Insira seu CPF:"))

while True:
    if Contas.Ver_CPF(cpf_user):
        print("CPF válido")
        break
    else:
        print("CPF inválido")
        cpf_user = str(input("Insira um CPF valido:"))
    
Email = str(input("Insira seu Email:"))

while True:
    if "@" in Email and "." in Email:
        print("Email válido")
        break
    else:
        print("Email inválido")
        Email = str(input("Insira um Email valido:"))

print(f"Tudo certo sr(a) {Nome}")
Tipo_Conta = str(input("Qual tipo de conta deseja criar? (Corrente ou Poupança):")).lower()

if Tipo_Conta == "1":  Tipo_Conta = "corrente"
elif Tipo_Conta == "2":  Tipo_Conta = "poupança"
while True:
    
    if Tipo_Conta not in ['corrente', 'poupança']:
        print("Tipo de conta inválido")
        Tipo_Conta = str(input("Qual tipo de conta deseja criar? (Corrente ou Poupança):"))
    else:
        print("Tipo de conta válido")
        break
if Tipo_Conta == 'poupança':
    print("Seus juros serão feitos mensalmente")

print(f"Conta {Tipo_Conta} criada com sucesso!")

saldo = 0.0
cheque = 500.0

while True:
    Contas.linha(100)
    print(f"Bem vindo sr(a) {Nome} \n \nSeu saldo atual é de {saldo}R$")
    Contas.linha(100)
    print("DEPÓSITO\n Adiciona dinheiro a sua conta")
    print("SAQUE\n retira dinheiro da sua conta")
    if Tipo_Conta in ['poupança']: 
        print("MESES\n a cada mês, você tem um lucro de +0,5%")
    
    if Tipo_Conta in ['corrente']: 
        print(f"\n\nVocê tem um cheque especial de {cheque}, que retira dinheiro\n extra da sua conta caso você não tenha, seu limite é de {cheque}R$\n")
    Contas.linha(100)
    Menu = str(input(f"O que você deseja fazer, {Nome}?:")).lower()


    if Menu == "meses" and Tipo_Conta in ['poupança']:
        try:
            messes = int(input("Quantos meses se passaram:"))
            lucro = (saldo * 0.05) * messes
            saldo = lucro + saldo
            print(f"\nVocê teve um lucro de {saldo}R$\n")
        except ValueError: print("\nEnsira um valor numerico!\n")
        
   
    elif Menu == "depósito":
        try:
            deposito = float(input("Quanto deseja depositar?"))
            saldo += deposito
            print(f"\nVocê adicionou +{deposito}R$ a sua conta\n")
        except ValueError: print("\nEscreva um valor em dinheiro!\n")
    
    elif Menu == "saque":
        try:
            saque = float(input("Quanto deseja sacar?"))
            if saque > saldo:
                print("Você não tem dinheiro suficiente")
                if Tipo_Conta in ['corrente']:
                    usarcheque = str(input("Deseja usar o cheque especial? S/N:")).lower()
                    if usarcheque in ['não', 'n'] or saque > saldo + cheque:
                        print("\nVocê precisa de mais dinheiro\n")
                    else:
                        cheque = cheque - (saque - saldo)
                        saldo = 0
                        print(f"\nVocê retirou -{saque}R$ da sua conta\n")
            else:
                print(f"\nVocê retirou -{saque}R$ da sua conta\n")
                saldo -= saque
        except ValueError: print("\nAlgo deu errado, tente novamente...\n")
    else:
        print("\nNão entendi o que você quer fazer... Escreva novamente\n")