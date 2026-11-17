# Exercício 6: Transferência de dados entre listas

usuarios_novos = ["Ana", "Carlos", "Beatriz"]
usuarios_ativos = []
while usuarios_novos:
    # Remove do final de novos e joga no final de ativos
    usuario = usuarios_novos.pop()
    usuarios_ativos.append(usuario)
print("Novos:", usuarios_novos)
print("Ativos:", usuarios_ativos)
