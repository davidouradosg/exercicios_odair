# Exercício 5: Caixa registradora (faturamento diário)

vendas_do_dia = []
for dia in range(1, 4):
    # Simulação de 3 vendas no dia
    vendas_do_dia.append(100.0)
    vendas_do_dia.append(50.5)
    vendas_do_dia.append(200.0)
    print(f"Total do Dia {dia}: R$ {sum(vendas_do_dia)}")
    vendas_do_dia.clear()  # começa o próximo dia do zero
