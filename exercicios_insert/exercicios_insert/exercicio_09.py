# Exercício 9: Simulando deslocamento de histórico

historico = ["google.com", "github.com"]
nova_pagina = "python.org"
historico.insert(0, nova_pagina)
if len(historico) > 3:
    historico.pop()  # Remove o mais antigo, no final
print(historico)  # Saída esperada: ['python.org', 'google.com', 'github.com']
