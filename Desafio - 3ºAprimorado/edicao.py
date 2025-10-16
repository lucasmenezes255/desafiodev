import os
import json
from time import sleep
from platform import system
from customtkinter import *

def tracinho():
    print('-'*50) 

def limpa_tela():
    if system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def tarefas_json():
    if not os.path.exists('tarefas.json'):
        return {'Pendente': {'ALTA': [], 'MÉDIA': [], 'BAIXA': []}, 'Executando': {'ALTA': [], 'MÉDIA': [], 'BAIXA': []}, 'Finalizado': {'ALTA': [], 'MÉDIA': [], 'BAIXA': []}}
    else:
        with open('tarefas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
        return dados

def edicoes(status, prioridade):
    print('='*50)
    print(f'{"MENU DE EDIÇÕES":^50}')
    print('='*50)
    print('[1] Mover Tarefa\n'
    '[2] Apagar Tarefa\n' 
    '[3] Sair\n'
    )
    prioridade_anterior = status
    prior_antiga = prioridade
    while True:  
        try:
            escolha = int(input('Escolha uma opção: '))
        except:
            print('Informação inválida! Selecione um valor do menu')
        else:
            if escolha not in [1, 2, 3]:
                print('Informação inválida! Selecione um valor do menu')
            else:
                break

    if escolha == 1:
        tarefas = tarefas_json()
        nome = str(input('Informe o título da tarefa que quer alterar: '))
        novo_status = str(input('Informe o novo status da tarefa: '))
        nova_prior = str(input('Informe a nova prioridade da tarefa: ')).upper().strip()
        for i in range(0,len(tarefas[prioridade_anterior])):
            for p in range(len(tarefas[prioridade_anterior][prior_antiga])):
                if tarefas[prioridade_anterior][prior_antiga][p]["Título"] == nome:
                    tarefa_copiada = tarefas[prioridade_anterior][prior_antiga][i]
                    tarefas[novo_status][nova_prior].append({'Título': tarefa_copiada['Título'], 'Descrição': tarefa_copiada['Descrição'], 'Status': novo_status, 'Prioridade': nova_prior})
                    del tarefas[prioridade_anterior][prior_antiga][i]
                    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                    tracinho()
                    sleep(2)
                    print('Tarefa movida com sucesso!')
                    if prioridade == 'Pendente':
                        from tarefas import tarefas_pendentes
                        tarefas_pendentes()
                    elif prioridade == 'Executando':
                        from tarefas import tarefas_executando
                        tarefas_executando()
                    elif prioridade == 'Finalizado':
                        from tarefas import tarefas_prontas
                        tarefas_prontas()

    elif escolha == 2:
        tarefas = tarefas_json()
        nome = str(input('Informe o título da tarefa que quer apagar: '))
        for i in range(0,len(tarefas[prioridade_anterior])):
            if tarefas[prioridade_anterior][prior_antiga][i]["Título"] == nome:
                del tarefas[prioridade_anterior][prior_antiga][i]
                tracinho()
                print('Tarefa apagada com sucesso!')
                break
        with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
            
    elif escolha == 3:
        print('Saindo')
        for i in range(3):
            print('.')
            sleep(1)
        from main import menu
        menu()