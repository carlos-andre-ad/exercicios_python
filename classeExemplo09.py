import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk



def criar_BD(db):
    try:
        connection = lite.connect(db)
        return connection
    except Error as captura:
        print("Esse BD já existe!")
        print(captura)
    finally:
        connection.close()


class Win(object):
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title('Usando Banco de dados SQLITE')
        texto = tk.Label(self.tela,text="Insira o nome do BD:")
        texto.pack()
        bd = tk.StringVar()
        nome_BD = tk.Entry(self.tela,textvariable=bd)
        nome_BD.pack()
        botao = tk.Button(self.tela, text="Criar Banco de Dados",
        command = criar_BD(bd.get()))
        botao.pack()
        self.tela.geometry("500x300")
        self.tela.mainloop()
win = Win()