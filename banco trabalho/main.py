import Dados as Contas

def linha(bar):
    print("-" * bar)

linha(50)
print("INFO BANK")
linha(50)

cadastro = str(input("Bem vindo, você ainda não está cadastrado. Deseja realizar o cadastro? S/N:"))

if cadastro == 'sim' or 'Sim' or 'S' or 's':
    print("Otimo")

else:
    print("Ok, encerrando o programa...")

print("Certo, proximo passo")

Nome = str(input("Insira seu nome:"))
cpf_user = str(input("Insira seu CPF:"))

if Contas.Ver_CPF(cpf_user):
    print("CPF válido")
else:
    print("CPF inválido")
    
Email = str(input("Insira seu Email:"))