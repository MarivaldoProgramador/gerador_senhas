import secrets
import PySimpleGUI as sg
import string


def gerar(tamanho):
    itens = (string.ascii_letters + string.digits + string.punctuation)
    senha = [secrets.choice(itens)  for i in range(tamanho)]
    senha = ''.join(senha)
    
    return senha


sg.theme("SystemDefault")
layout = [
    [sg.Text('Tamanho', size=(25, 1))],
    [sg.Input(key="tamanho", size=(20, 1))],
    [sg.Button('Gerar')],
    [sg.Text(" ", key="mensagem")]
]

janela = sg.Window("Gerador", layout=layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == "Gerar":
        try:
            tamanho = int(valores['tamanho'])
        except ValueError:
            janela['mensagem'].update("Ops! Algo deu errado.")
        else:
            janela['mensagem'].update(f"Sua senha: {gerar(tamanho)}")

janela.close()