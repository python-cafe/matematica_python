# Desvendando a matemática com Python #3
# Representação de Matrizes

# Lista de listas
# matriz = [[1, 6, 9],
#           [3, 7, 2],
#           [8, 8, 0],
#           [9, 5, 7]]

def exibir_matriz(matriz):
    """Exibe uma matriz na saída padrão"""
    for linha in matriz:
        print(linha)

# Pedindo os elementos, um a um, ao usuário
m = int(input("Número de linhas: "))
n = int(input("Número de colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = input("Elemento da linha {} e coluna {}".format(i, j))
        linha.append(float(elemento))
    matriz.append(linha)

exibir_matriz(matriz)

# Criando uma matriz a partir de um arquivo de texto
matriz = []

arquivo = open("matriz4x5.txt", "r")
linha = arquivo.readline()
while linha!= "":
    elementos = linha.split()
    for n in range(len(elementos)):
        elementos[n] = float(elementos[n])
    matriz.append(elementos)
    linha = arquivo.readline()

arquivo.close()

exibir_matriz(matriz)

# Obs: Se você entende List Comprehension em Python, as linhas 36 e 37 poderiam
# ser escritas assim: elementos = [float(e) for e in elementos]
