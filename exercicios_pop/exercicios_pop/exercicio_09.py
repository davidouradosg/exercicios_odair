# Exercício 9: Jogo de cartas - sorteando e removendo

baralho = ["Ás", "Rei", "Valete", "Dama"]
indice = int(input("Escolha uma carta pelo índice (0 a 3): "))
if 0 <= indice < len(baralho):
    carta_comprada = baralho.pop(indice)
    print(f"Você comprou a carta: {carta_comprada}")
    print("Cartas restantes no baralho:", baralho)
else:
    print("Índice inválido!")
