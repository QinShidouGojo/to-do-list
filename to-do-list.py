# CRIAR TO-DO LIST
# Preciso de um sistema de to-do list
# Preciso conseguir inserir uma nova tarefa
# Deletar uma tarefa específica
# Consultar a lista de tarefas
# Alterar uma tarefa existente
# Os dados serão alimentados por input do usuário


tarefas = []
tarefas_encontradas = []

def inserir_tarefa():
    resposta4 = input("""
        Escolha dentre as opções:
        1 - Adicionar tarefa
        2 - Voltar
        """)
    if resposta4 == str(1):
        tarefa_adicionada = input("Tarefa que deseja adicionar: ")
        tarefas.append(tarefa_adicionada)
    elif resposta4 == str(2):
        home()
    else:
        print("Escolha entre os numeros de 1 e 2!")

def deletar_tarefa():
    resposta5 = int(input("""
        Escolha dentre as opções:
        1 - Deletar tarefa
        2 - Voltar
        """))
    
    print("""
            
    Suas tarefas atuais são: 
    """)
    task_num = 1
    for task in tarefas:
        print(f"{task_num} - {task}")
        task_num = task_num + 1

    if resposta5 == 1:
        tarefa_a_deletar = int(input("Número da tarefa que deseja deletar: "))
        numero_tarefa = tarefa_a_deletar - 1
        tarefas.pop(numero_tarefa)
    elif resposta5 == 2:
        home()
    else:
        print("Escolha entre os numeros de 1 e 2!")

# Filtragem adicional
def buscar_tarefas():
    nome_tarefa = input("Insira a tarefa que deseja encontrar: ")
    tarefas_encontradas.clear()

    inicial = False
    for task in tarefas:
        if nome_tarefa in task:
            inicial = True
    if inicial == False:
        print("Nenhuma tarefa correspondente")
        home()

    print("As tarefas correspondentes são: ")
    for task in tarefas:
        if nome_tarefa in task:
            tarefas_encontradas.append(task)

    task_num = 1
    for task in tarefas_encontradas:
        print(f"{task_num} - {task}")
        task_num = task_num + 1

    resposta8 = input("""
        Escolha dentre as opções:
        1 - Marcar tarefa
        2 - Voltar
        """)
    
    if resposta8 == str(1):
        tarefa_a_marcar = int(input("Número da tarefa que deseja marcar: "))
        numero_a_marcar = tarefa_a_marcar - 1
        nome_tarefa_puro = tarefas_encontradas[numero_a_marcar]
        if nome_tarefa_puro in tarefas:
            indice = tarefas.index(nome_tarefa_puro)
        tarefas[indice] = tarefas[indice] + " (Completada)"

    elif resposta8 == str(2):
        home()

def alterar_tarefa():
    resposta6 = int(input("""
        Escolha dentre as opções:
        1 - Alterar tarefa
        2 - Voltar
        """))
    
    print("""
            
    Suas tarefas atuais são: 
    """)
    task_num = 1
    for task in tarefas:
        print(f"{task_num} - {task}")
        task_num = task_num + 1

    if resposta6 == 1:
        tarefa_a_alterar = int(input("Número da tarefa que deseja alterar: "))
        numero_tarefa2 = tarefa_a_alterar - 1
        tarefas.pop(numero_tarefa2)
        tarefa_alterada = input("Tarefa alterada: ")
        tarefas.append(tarefa_alterada)
    elif resposta6 == 2:
        home()
    else:
        print("Escolha entre os numeros de 1 e 2!")

def consultar_tarefas():
    print("""
            
    Suas tarefas são: 
    """)
    task_num = 1
    for task in tarefas:
        print(f"{task_num} - {task}")
        task_num = task_num + 1

    print("""
        Escolha dentre as opções:
        1 - Buscar por tarefa
        2 - Marcar tarefa
        3 - Voltar
          
        """)

    resposta2 = int(input("Sua resposta: "))
    print(resposta2)

    print("""          
    Suas tarefas atuais são: 
    """)
    task_num = 1
    for task in tarefas:
        print(f"{task_num} - {task}")
        task_num = task_num + 1
    
    if resposta2 == (1):
        buscar_tarefas()
    elif resposta2 == str(2):
        tarefa_a_marcar = int(input("Número da tarefa que deseja marcar: "))
        numero_a_marcar = tarefa_a_marcar - 1
        tarefas[numero_a_marcar] = tarefas[numero_a_marcar] + " (Completada)"
    elif resposta2 == str(3):
        home()

def home():
    rodando = True
    while rodando == True:
        print("""
              
        Escolha dentre as opções:
        1 - Inserir tarefa
        2 - Deletar tarefa
        3 - Lista de tarefas
        4 - Sair
        """)

        resposta = input("Sua escolha: ")

        if resposta == str(1):
            inserir_tarefa()
        elif resposta == str(2):
            deletar_tarefa()
        elif resposta == str(3):
            consultar_tarefas()
        elif resposta == str(4):
            print("Você Saiu!")
            rodando = False
        else:
            print("Escolha entre os numeros de 1 a 4!")
            continue

home()
