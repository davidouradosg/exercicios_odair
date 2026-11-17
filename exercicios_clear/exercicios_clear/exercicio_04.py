# Exercício 4: Clear vs atribuição (referência de memória)

original = [1, 2, 3]
copia = original  # copia aponta para o MESMO objeto
original.clear()
print("Cópia também foi limpa:", copia)
