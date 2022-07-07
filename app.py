import PySimpleGUI  as sg
import pandas as pd

tabela = pd.read_excel("DataBase.xlsx")

tabela = pd.read_excel("DataBase.xlsx")
sg.theme('Reddit')

layout = [  
    [sg.Text('Sistema de Login')],
    [sg.Text('Usuario'), sg.InputText(key="Usuario")],
    [sg.Text('Senha'), sg.InputText(key="Senha")],
    [sg.Button('Entrar'), sg.Button('Salvar Novo Usuario')] 
]

janela = sg.Window('Login', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
        
    if event == "Salvar Novo Usuario":
        df = pd.DataFrame(tabela)
        new_row = {'Usuarios': values['Usuario'],'Senhas':values['Senha'],}
        df = df.append(new_row, ignore_index=True)#Adiciona linha do novo usuario
        df.to_excel("DataBase.xlsx")#Exporta
        break



janela.close()
