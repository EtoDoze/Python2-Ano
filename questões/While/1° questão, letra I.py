num1 = 0
num2 = 1
contador = 1

print("A sua sequencia é:")
while contador <= 34:
    num3 = num1 + num2
    print(num3, "termo:", contador)
    num1 = num2
    num2 = num3
    contador += 1