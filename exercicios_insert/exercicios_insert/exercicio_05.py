# Exercício 5: Mantendo uma lista ordenada

valores = [10, 20, 30, 40]
novo_valor = int(input("Digite um número (ex.: 25): "))

# Descobrindo a posição correta dinamicamente
posicao = 0
for i, num in enumerate(valores):
    if novo_valor > num:
        posicao = i + 1

valores.insert(posicao, novo_valor)
print(valores)  # Com 25: [10, 20, 25, 30, 40]
