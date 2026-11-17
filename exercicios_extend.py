# Exercícios Práticos: Método extend() em Python

# --- Exercício 1: Juntando duas listas de compras ---
print("Exercício 1")
feira = ["maçã", "banana"]
limpeza = ["detergente", "sabão"]
feira.extend(limpeza)
print(feira)

# --- Exercício 2: Adicionando uma tupla a uma lista ---
print("\nExercício 2")
numeros = [1, 2, 3]
novos_numeros = (4, 5, 6)
numeros.extend(novos_numeros)
print(numeros)

# --- Exercício 3: Combinando listas de alunos ---
print("\nExercício 3")
turma_a = ["Ana", "Bruno"]
turma_b = ["Carlos", "Diana"]
turma_c = ["Eduarda", "Fábio"]
todos_alunos = []
todos_alunos.extend(turma_a)
todos_alunos.extend(turma_b)
todos_alunos.extend(turma_c)
print(todos_alunos)

# --- Exercício 4: Diferença entre append e extend ---
print("\nExercício 4")
lista_1 = [1, 2]
lista_1.append([3, 4])  # Cria uma lista aninhada
lista_2 = [1, 2]
lista_2.extend([3, 4])  # Adiciona os elementos individualmente
print("Com append:", lista_1)
print("Com extend:", lista_2)

# --- Exercício 5: Processando lotes de dados ---
print("\nExercício 5")
lotes = [[100, 150], [200, 80], [300, 450]]
historico_vendas = []
for lote in lotes:
    historico_vendas.extend(lote)
print(historico_vendas)

# --- Exercício 6: Copiando elementos filtrados por lote ---
print("\nExercício 6")
dados = [[1, 5, 12], [8, 20, 3], [15, 7]]
maiores_que_cinco = []
for sublista in dados:
    temp = [num for num in sublista if num > 5]
    maiores_que_cinco.extend(temp)
print(maiores_que_cinco)

# --- Exercício 7: Unificando letras de palavras ---
print("\nExercício 7")
letras = []
letras.extend("Python")
print(letras)

# --- Exercício 8: Mesclando as chaves de um dicionário ---
print("\nExercício 8")
lista_chaves = ["id", "nome"]
novos_dados = {"email": "user@email.com", "idade": 25}
lista_chaves.extend(novos_dados.keys())
print(lista_chaves)

# --- Exercício 9: Gerador de sequências numéricas ---
print("\nExercício 9")
sequencia = []
for _ in range(3):
    sequencia.extend([1, 2, 3])
print(sequencia)

# --- Exercício 10: Consolidando uma fila de tarefas ---
print("\nExercício 10")
fila_execucao = ["Tarefa Inicial"]
entrada = input("Digite duas tarefas separadas por vírgula: ")
# Exemplo de entrada: Estudar Python, Lavar a louça
novas_tarefas = [t.strip() for t in entrada.split(",")]
fila_execucao.extend(novas_tarefas)
print(fila_execucao)
