# Exercício 5 - Separando palavras por tamanho
palavras = ["sol", "computador", "lua", "paralelepípedo", "pai"]
grandes = []
for p in palavras:
    if len(p) > 4:
        grandes.append(p)
print(grandes)
