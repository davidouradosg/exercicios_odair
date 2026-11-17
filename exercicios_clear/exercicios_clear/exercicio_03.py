# Exercício 3: Ciclo de processamento de buffers

buffer = []
for i in range(1, 6):
    buffer.append(i)
    if len(buffer) == 5:
        print("Processando dados...", buffer)
        buffer.clear()
print("Buffer limpo:", buffer)
