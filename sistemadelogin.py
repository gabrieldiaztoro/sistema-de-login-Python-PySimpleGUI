import PySimpleGUI as sg

layout = [
    [sg.Text("Usuário")],
    [sg.Input(key="usuario")],
    [sg.Text("Senha")],
    [sg.Input(key="senha")],
    [sg.Button("Login")],
    [sg.Text(key="mensagem")],
]

window = sg.Window("Login", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
