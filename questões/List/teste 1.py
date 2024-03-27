A = []
B = []

for i in range(0,5):
    A.append(int(input("insira um valor:")))
    if (i) % 2 == 0:
        B.append(A[i] * 5)
    else:
        B.append(A[i] + 5)
print(A)
print(B)