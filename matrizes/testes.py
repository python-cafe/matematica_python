from representacao_matrizes import ler_matriz, exibir_matriz
from operacoes import *

A = ler_matriz("matriz2x4.txt")
B = ler_matriz("matriz4x5.txt")
C = ler_matriz("matriz_soma4x5.txt")

# matriz A é igual a ela mesma?
if (eh_igual(A, A)):
    exibir_matriz(A)
    print("Matriz A é igual a matriz A")
else:
    print("Erro na funcao eh_igual")

# matriz A é igual a sua transposta ?
print("*************")
T = transposta(A)
exibir_matriz(A)
print("-----------")
exibir_matriz(T)
if (eh_igual(A, T)):
    print("Deu erro na funcao igual ou na transposta")
else:
    print("Legal, elas são diferentes mesmo")

# transposta da transposta é igual à original?
print("*************")
P = transposta(T)
exibir_matriz(A)
print("-----------")
exibir_matriz(P)
if (eh_igual(A, P)):
    print("Legal, transposta de trasnposta é a original")
else:
    print("Deu erro")

print("*************")
transposta_depois = transposta(somar(B, C))
transposta_antes = somar(transposta(B), transposta(C))
exibir_matriz(transposta_antes)
print("-----------")
exibir_matriz(transposta_depois)
if(eh_igual(transposta_antes, transposta_depois)):
    print("Sucesso, tudo conforme o esperado")
else:
    print(":(")