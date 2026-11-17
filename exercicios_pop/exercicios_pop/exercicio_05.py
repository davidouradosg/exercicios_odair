# Exercício 5: Esvaziando uma lista com while

pedidos = ["Pedido #1", "Pedido #2", "Pedido #3"]
while len(pedidos) > 0:
    pedido_processado = pedidos.pop(0)
    print(f"Processando {pedido_processado}...")
print("Todos os pedidos foram processados!")
