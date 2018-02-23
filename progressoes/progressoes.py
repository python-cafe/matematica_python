# Progressões Aritméticas | Matemática com Python
# Python Café - Hallison Paz


def pa_termo(a0, r, n):
    return a0 + n*r

def pa_soma(a0, r, n):
    soma = 0
    for i in range(n+1):
        soma = soma + pa_termo(a0, r, n)
    return soma


termo_inicial = int(input("Termo inicial da PA: "))
razao = int(input("Razão da PA: "))
n = int(input("Posição (N): "))

print("N-ésimo termo:", pa_termo(termo_inicial, razao, n))
print("Soma da PA:", pa_soma(termo_inicial, razao, n))
