list = [1,2,3,4,5]
resp = "se quiser sim"

while True:
    n=(int(input("digite um numero para procurar na lista poha ")))
    if n in list:
        print("O numero", n , "esta na lista caralho ")
    else:
        print("ta nao boy kk")
        resp = int(input("deseja esclher outro numero? kk "))
    if resp=="nao":
        break
print("fimmm")

