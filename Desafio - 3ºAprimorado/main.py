from tarefas import criar_tarefa, tarefas_gerais, tarefas_executando, tarefas_pendentes, tarefas_prontas, limpa_tela
from time import sleep
from customtkinter import *

def menu():
    janela_menu = CTk()
    janela_menu.title('Desafio Dev')
    janela_menu.geometry('700x400')
    janela_menu.resizable(width=False, height=False)
    janela_menu._set_appearance_mode('system')
    texto_menu = CTkLabel(janela_menu, text='MENU DE TAREFAS', height=70).pack()

    cria_tarefa = CTkButton(janela_menu, text='CRIAR TAREFA', command=criar_tarefa).pack(pady=10)
    tarefas = CTkButton(janela_menu, text='VER TODAS AS TAREFAS', command=tarefas_gerais).pack(pady=10)
    pendentes = CTkButton(janela_menu, text='VER TAREFAS PENDENTES', command=tarefas_pendentes).pack(pady=10)
    executando = CTkButton(janela_menu, text='VER TAREFAS EM EXECUÇÃO', command=tarefas_executando).pack(pady=10)
    prontas = CTkButton(janela_menu, text='VER TAREFAS PRONTAS', command=tarefas_prontas).pack(pady=10)
    sair = CTkButton(janela_menu, text='SAIR', command=janela_menu.destroy).pack(pady=10)
    
    janela_menu.mainloop()

if __name__ == "__main__":
    menu()