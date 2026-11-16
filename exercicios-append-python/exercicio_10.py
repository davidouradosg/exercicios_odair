# Exercício 10 - Acumulador de valores até uma condição
numeros_digitados = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros_digitados.append(num)
print(numeros_digitados)
