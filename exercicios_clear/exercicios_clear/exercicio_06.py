# Exercício 6: Sistema de cadastro com confirmação

novos_produtos = []
for i in range(3):
    produto = input(f"Digite o produto {i + 1}: ")
    novos_produtos.append(produto)

opcao = input("Deseja salvar os produtos? (S/N): ").upper()
if opcao == "N":
    novos_produtos.clear()
    print("Operação cancelada. Lista limpa.")
else:
    print("Produtos salvos:", novos_produtos)
