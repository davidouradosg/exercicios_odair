# Exercício 8: Monitoramento de logs por lote

logs = []
logs.append("Erro 404")
logs.append("Erro 500")
logs.append("Erro 403")
logs.append("Erro 502")

if len(logs) == 4:
    print("Enviando lote de logs ao servidor...")
    logs.clear()
print("Status atual dos logs:", logs)
