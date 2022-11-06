from key import chave_api
import requests
import pandas as pd
from tkinter import *


def cotacao():
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={en_token.get()}.SAO&apikey={chave_api}'
    r = requests.get(url)
    data = r.json()
    lst = [list(data['Global Quote'].keys()),
           list(data['Global Quote'].values())]
    total_rows = len(lst)
    total_columns = len(lst[0])

    numero_linhas = 1
    numero_colunas = 1
    for i in range(total_rows):
        for j in range(total_columns):
            texto_tabela = Entry(
                janela, width=17, font=('Garamond', 11))
            texto_tabela.grid(column=numero_colunas, row=numero_linhas)
            texto_tabela.insert(END, lst[i][j])
            numero_colunas += 1
        numero_linhas += 1
        numero_colunas = 1


janela = Tk()
janela.title("Consulta Ação")

texto_orientacao = Label(
    janela, text="Escreva a ação que deseja efetuar a cotação:")
texto_orientacao.grid(column=0, row=0)

en_token = Entry(
    janela, bd=2, font=("Garamond", 14), justify=CENTER)
en_token.grid(column=0, row=1)

bt_entrar = Button(
    janela, text="Consultar", command=cotacao)
bt_entrar.grid(column=0, row=2)

janela.mainloop()
