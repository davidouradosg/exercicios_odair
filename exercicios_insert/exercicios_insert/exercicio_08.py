# Exercício 8: Preenchendo espaços vazios (zeros à esquerda)

dados = [99, 100]
while len(dados) < 5:
    dados.insert(0, 0)
print(dados)  # Saída esperada: [0, 0, 0, 99, 100]
