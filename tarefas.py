import json
import os
from platform import system
from time import sleep
from edicao import edicoes, tarefas_json
from customtkinter import *


def limpa_tela():
    if system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def tracinho():
    print('-'*50)


def tarefas_pendentes():
    tarefas = tarefas_json()
    '''
    pendentes = CTk()
    pendentes.title('Desafio Dev')
    pendentes.geometry('700x400')
    pendentes.resizable(width=False, height=False)
    pendentes._set_appearance_mode('system')
    texto_menu = CTkLabel(pendentes, text='TAREFAS PENDENTES', height=70).pack()

    prioridade_alta = CTkFrame(pendentes,width=200, height=250).place(x=20, y=80)
    '''
    '''
    for i in range(0, len(tarefas['Pendente'])):                      TRECHO DO CÓDIGO A SER TRABALHADO PARA LISTAR AS TAREFAS
        for p in range(3):
            if p == 0:
                p = 'ALTA'
            elif p == 1:
                p = 'MÉDIA'
            elif p == 2:
                p = 'BAIXA'
            tarefa = f'+{i+1}. Título: {tarefas["Pendente"][p][i]["Título"]}\n   Descrição: {tarefas["Pendente"][p][i]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][p][i]["Prioridade"]}'
            tarefas_alta = CTkLabel(pendentes, text=tarefa)
    prioridade_media = CTkFrame(pendentes,width=200, height=250).place(x=250, y=80)

    prioridade_baixa = CTkFrame(pendentes,width=200, height=250).place(x=480, y=80)
    '''
    '''
    from main import menu
    botao_lista = CTkButton(pendentes, text='ESCOLHER OUTRA LISTA', command=menu).place(x=100,y=340)
    botao_saida = CTkButton(pendentes, text='SAIR', command=pendentes.destroy).place(x=400,y=340)
    pendentes.mainloop()
    '''

    limpa_tela()
    tarefas = tarefas_json()
    print('='*50)
    print(f'{"LISTA DE TAREFAS":^50}')
    print('='*50)
    print(f'{" TAREFAS PENDENTES ":-^50}')
    if len(tarefas['Pendente']) == 0:
        print('Não há tarefas para essa lista!')
        tracinho()
        while True:
            escolha = str(
                input('Escolher outra lista? [S/N]: ')).upper().strip()
            if escolha == 'S':
                from main import menu
                menu()
            elif escolha == 'N':
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpa_tela()
                break
            else:
                print('Informação inválida, tente novamente!')
    else:
        print('')
        for i in range(0, len(tarefas['Pendente'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break                      
                
                
        while True:
                escolha = str(
                    input('Deseja ver alterações? [S/N]: ')).upper().strip()
                if escolha == 'S':
                    pendente = 'Pendente'
                    edicoes(pendente, prio)
                    break
                elif escolha == 'N':
                    tracinho()
                    print('Saindo')
                    for i in range(3):
                        print('.')
                        sleep(1)
                    from main import menu
                    menu()
                    break
                else:
                    print('Informação inválida, tente novamente!')
    

def tarefas_executando():
    limpa_tela()
    tarefas = tarefas_json()
    print('='*50)
    print(f'{"LISTA DE TAREFAS":^50}')
    print('='*50)
    print(f'{" TAREFAS EXECUTANDO ":-^50}')
    if len(tarefas['Executando']) == 0:
        print('Não há tarefas para essa lista!')
        tracinho()
        while True:
            escolha = str(
                input('Escolher outra lista? [S/N]: ')).upper().strip()
            if escolha == 'S':
                from main import menu
                menu()
            elif escolha == 'N':
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpa_tela()
                break
            else:
                print('Informação inválida, tente novamente!')

    else:
        print('')
        for i in range(0, len(tarefas['Executando'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break

        while True:
                escolha = str(
                    input('Deseja ver alterações? [S/N]: ')).upper().strip()
                if escolha == 'S':
                    executando = 'Executando'
                    edicoes(executando, prio)
                    break
                elif escolha == 'N':
                    tracinho()
                    print('Saindo')
                    for i in range(3):
                        print('.')
                        sleep(1)
                    from main import menu
                    menu()
                    break
                else:
                    print('Informação inválida, tente novamente!')


def tarefas_prontas():
    limpa_tela()
    tarefas = tarefas_json()
    print('='*50)
    print(f'{"LISTA DE TAREFAS":^50}')
    print('='*50)
    print(f' {"TAREFAS FINALIZADAS":-^50} ')
    if len(tarefas['Finalizado']) == 0:
        print('Não há tarefas para essa lista!')
        tracinho()
        while True:
            escolha = str(
                input('Escolher outra lista? [S/N]: ')).upper().strip()
            if escolha == 'S':
                from main import menu
                menu()
            elif escolha == 'N':
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpa_tela()
                break
            else:
                print('Informação inválida, tente novamente!')

    else:
        print('')
        for i in range(0, len(tarefas['Finalizado'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][i]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break

        while True:
                escolha = str(
                    input('Deseja ver alterações? [S/N]: ')).upper().strip()
                if escolha == 'S':
                    finalizado = 'Finalizado'
                    edicoes(finalizado, prio)
                    break
                elif escolha == 'N':
                    tracinho()
                    print('Saindo')
                    for i in range(3):
                        print('.')
                        sleep(1)
                    from main import menu
                    menu()
                    break
                else:
                    print('Informação inválida, tente novamente!')

def tarefas_em_teste():
    limpa_tela()
    tarefas = tarefas_json()
    print('='*50)
    print(f'{"LISTA DE TAREFAS":^50}')
    print('='*50)
    print(f' {"TAREFAS FINALIZADAS":-^50} ')
    if len(tarefas['Finalizado']) == 0:
        print('Não há tarefas para essa lista!')
        tracinho()
        while True:
            escolha = str(
                input('Escolher outra lista? [S/N]: ')).upper().strip()
            if escolha == 'S':
                from main import menu
                menu()
            elif escolha == 'N':
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpa_tela()
                break
            else:
                print('Informação inválida, tente novamente!')

    else:
        print('')
        for i in range(0, len(tarefas['Em Teste'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Em Teste"][prio][qt]["Título"]}\n   Descrição: {tarefas["Em Teste"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Em Teste"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][i]["Descrição"]}\n   Prioridade: {tarefas["Em Teste"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Em Teste'][prio])):
                        print(f'{i+1}. Título: {tarefas["Em Teste"][prio][qt]["Título"]}\n   Descrição: {tarefas["Em Teste"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Em Teste"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break

        while True:
                escolha = str(
                    input('Deseja ver alterações? [S/N]: ')).upper().strip()
                if escolha == 'S':
                    em_teste = 'Em Teste'
                    edicoes(em_teste, prio)
                    break
                elif escolha == 'N':
                    tracinho()
                    print('Saindo')
                    for i in range(3):
                        print('.')
                        sleep(1)
                    from main import menu
                    menu()
                    break
                else:
                    print('Informação inválida, tente novamente!')


def tarefas_gerais():
    limpa_tela()
    tarefas = tarefas_json()
    print('='*50)
    print(f'{"LISTA DE TAREFAS":^50}')
    print('='*50)
    print(f'{" TAREFAS PENDENTES ":-^50}')
    if len(tarefas['Pendente']) == 0:
        print('')
        print('Sem tarefas pendentes!')
        tracinho()
    else:
        for i in range(0, len(tarefas['Pendente'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Pendente'][prio])):
                        print(f'{i+1}. Título: {tarefas["Pendente"][prio][qt]["Título"]}\n   Descrição: {tarefas["Pendente"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Pendente"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break 
    print(f'{" TAREFAS EXECUTANDO ":-^50}')
    if len(tarefas['Executando']) == 0:
        print('')
        print('Sem tarefas executadas!')
        tracinho()
    else:
        for i in range(0, len(tarefas['Executando'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Executando'][prio])):
                        print(f'{i+1}. Título: {tarefas["Executando"][prio][qt]["Título"]}\n   Descrição: {tarefas["Executando"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Executando"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break

    print(f'{" TAREFAS FINALIZADAS ":-^50}')
    if len(tarefas['Finalizado']) == 0:
        print('')
        print('Sem tarefas finalizadas')
        tracinho()
    else:
        for i in range(0, len(tarefas['Finalizado'])): 
            if i == 0:
                prio = 'ALTA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                prio = 'MÉDIA'
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                prio = 'BAIXA' 
                while True:
                    for qt in range(0, len(tarefas['Finalizado'][prio])):
                        print(f'{i+1}. Título: {tarefas["Finalizado"][prio][qt]["Título"]}\n   Descrição: {tarefas["Finalizado"][prio][qt]["Descrição"]}\n   Prioridade: {tarefas["Finalizado"][prio][qt]["Prioridade"]}')
                        tracinho()  
                    break
    while True:
        escolha = str(
        input('Voltar para o menu? [S/N]: ')).upper().strip()
        if escolha == 'S':
            from main import menu
            menu()
        elif escolha == 'N':
            print('Saindo')
            for i in range(3):
                print('.')
                sleep(1)
                limpa_tela()
                break
        else:
            print('Informação inválida, tente novamente!')
        break
    
def criar_tarefa():
    tarefas = tarefas_json()
    tracinho()
    while True:
        titulo = str(input('Informe o título da tarefa: ')).strip()
        if titulo == "":
            print('ERRO! O título não pode ser vazio')
            tracinho()
        else:
            break
    while True:
        descricao = str(input('Informe os detalhes da tarefa: ')).strip()
        if descricao == "":
            print('ERRO! A descrição não pode ser vazia')
            tracinho()
        else:
            break
    while True:
        if len(descricao) <= 1000:
            if len(descricao) == 1000:
                print('ERRO: Limite de caracteres atingido')
                continua = str(input('Reescrever a descrição da atividade? [S/N]: ')).upper().strip()
                if continua == 'S':
                    tracinho()
                    descricao = str(input('Informe os detalhes da tarefa: ')).strip()
                elif continua == 'N':
                    print('Saindo...')
                    sleep(1)
                    limpa_tela()
                    break
            else:
                while True:
                    prioridade = str(input('Informe a prioridadea da tarefa: ')).upper().strip()
                    if prioridade == "ALTA" or prioridade == "MÉDIA" or prioridade == "BAIXA":
                        break
                    else:
                        print('ERRO! Prioridade escrita de maneira errada')
                        tracinho()
                tarefas['Pendente'][prioridade].append({'Título': titulo, 'Descrição': descricao, 'Status': 'Pendente', 'Prioridade': prioridade})
                with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                tracinho()
                print('Tarefa adiciona ao campo "Pendentes" com sucesso!')
                sleep(1)
                from main import menu
                menu()
                break
        else:
            print('ERRO: Limite de caracteres atingido')
            continua = str(input('Reescrever a descrição da atividade? [S/N]: ')).upper().strip()
            if continua == 'S':
                tracinho()
                descricao = str(input('Informe os detalhes da tarefa: ')).strip()
                break
            elif continua == 'N':
                tracinho()
                while True:
                    escolha = str(input('Voltar para o menu? [S/N]: ')).upper().strip()
                    if escolha == 'S':
                        from main import menu
                        menu()
                    elif escolha == 'N':
                        print('Saindo')
                        for i in range(3):
                            print('.')
                            sleep(1)
                        limpa_tela()
                        break
                    else:
                        print('Informação inválida, tente novamente!')
                break
            else:
                print('Informação inválida, tente novamente!')
            break