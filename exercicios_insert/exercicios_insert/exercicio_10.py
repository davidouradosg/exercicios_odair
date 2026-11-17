# Exercício 10: Inserindo marcadores entre elementos

etapas = ["Planejar", "Executar", "Revisar"]
fluxo = etapas.copy()
# Inserindo de trás para frente para não bagunçar os índices
fluxo.insert(2, "-->")
fluxo.insert(1, "-->")
print(fluxo)  # Saída esperada: ['Planejar', '-->', 'Executar', '-->', 'Revisar']
