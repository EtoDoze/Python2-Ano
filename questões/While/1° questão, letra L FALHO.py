cont = 1
fatorial = 1

    
#while cont <= 15:
 #   num1 = int(input("insira outro:")) 
  #  fatorial = fatorial * num1
   # num1 = num1 - 1
    #print("você tem", cont,"/15 de vezes ainda, fatorial:", fatorial)
    #cont = cont + 1
#print("somatorio:", fatorial)
while cont <= 15:
    num1 = int(input("insira outro:")) 
    while num1 > 0:
        fatorial = fatorial * num1
        num1 = num1 - 1
    print(fatorial)