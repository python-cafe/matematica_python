# Desvendando a matemática com Python #5
# Operações com matrizes: adição, subtração
# Lista de listas
# matriz = [[1, 6, 9],
#           [3, 7, 2],
#           [8, 8, 0],
#           [9, 5, 7]]

def somar(A, B):
    C = []
    #verificar se A e B tem a mesma
    nLinhasA, nLinhasB = len(A), len(B)
    nColA, nColB = len(A[0]), len(B[0])
    if (nLinhasA == nLinhasB) and (nColA == nColB):
        # posso somar
        for i in range(nLinhasA):
            linha = [0]*nColA
            C.append(linha)
            for j in range(nColA):
                C[i][j] = A[i][j] + B[i][j]
    else:
        print("Matrizes não tem a mesma ordem")

    return C


def oposta(M):
    op = []
    for i in range(len(M)):
        linha = [0]*len(M[0])
        op.append(linha)
        for j in range(len(M[0])):
            op[i][j] = -M[i][j]
    return op

def subtrair(A, B):
    return somar(A, oposta(B))


matriz1 = [[1, 6, 9],
          [3, 7, 2],
          [8, -8, 0],
          [-9, 5, 7]]

matriz2 = [[10, 4, 9],
          [-5, -7, 0],
          [0, 2, -12],
          [8, 8, 0]]