# Exercício 7: Evitando erro de índice vazio (IndexError)

def remover_seguro(lista):
    if len(lista) > 0:
        return lista.pop()
    else:
        print("Erro: A lista já está vazia!")
        return None


itens = []
remover_seguro(itens)
