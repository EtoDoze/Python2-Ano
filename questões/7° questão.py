Nome = str(input("qual seu nome? "))
Genero = str(input("qual seu sexo? "))

if Genero == str("Homem" or "Masculino"):
    print("Saudações",Nome,"ilmo Sr, espero que o senhor esteja tendo um otimo dia :)")
    
elif Genero == str("Mulher" or "Feminino"):
    print("Saudações",Nome,"ilmo Sra, espero que a senhorita esteja tendo um otimo dia :)")
    
else:
    print("Senhor(a)", Nome ,"A maquina não conseguiu definir seu sexo, por favor tente ver se não foi um erro de escrita.")