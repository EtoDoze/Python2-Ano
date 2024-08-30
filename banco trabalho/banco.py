def linha(bar):
    print("-" * bar)

linha(50)
print("INFO BANK")
linha(50)

cadastro = str(input("Bem vindo, você ainda não está cadastrado. Deseja realizar o cadastro? S/N:"))

if cadastro == 'sim' or 'Sim' or 'S' or 's':
    print("Otimo")
    nome = str(input("Qual seu nome?:"))

else:
    print("Ok, encerrando o programa...")

print(f"Certo, Sr {nome}")