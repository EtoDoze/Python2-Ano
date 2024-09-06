import numpy as np

# Criando um array
arr = np.array([1, 2, 3, 4, 5])

# Operações com o array

print(arr.mean()) # Calcula a média

print(arr * 2) # Multiplica cada elemento por 2

# Criando uma matriz

matriz = np.array([[1, 2], [3, 4]])

# Operações com a matriz

print(matriz.T) # Transposta da matriz
print(np.dot(matriz, matriz)) # Multiplicação de matrizes