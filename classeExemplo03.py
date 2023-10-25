from tkinter import *


class Application:
    def __init__(self, master=None):
        janela.title("Criando janela com Orientação a Objeto - Classe")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg = Label(self.tela1, text="Hello Wordl")
        self.msg.pack()
        self.botao = Button(self.tela1, text="Fechar",command=self.tela1.quit)
        self.botao.pack()
janela = Tk()
janela.geometry("500x300")
Application(janela)
janela.mainloop()

