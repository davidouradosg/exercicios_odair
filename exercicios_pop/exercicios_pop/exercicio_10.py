# Exercício 10: Separando ímpares e pares dinamicamente

valores = [11, 22, 33, 44, 55]
impares = []
# Iterando de trás para frente para evitar problemas ao remover
for i in range(len(valores) - 1, -1, -1):
    if valores[i] % 2 != 0:
        impares.append(valores.pop(i))
print("Valores restantes (apenas pares):", valores)
print("Valores removidos (ímpares):", impares)
