# Exercício 7: Inserção dinâmica com entrada do usuário

nomes = ["Bruna", "Diego", "Gabriel"]
novo_nome = input("Digite um nome: ")
posicao = int(input(f"Digite a posição de 0 a {len(nomes)}: "))
nomes.insert(posicao, novo_nome)
print(nomes)
