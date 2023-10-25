import tkinter

class Application:
    def __init__(self, master=None):
        janela.title("Criando janela com Orientação a Objeto - Classe")
        botao = tkinter.Button(janela, text="CLASSE",fg="blue")
        botao.pack()
        
janela = tkinter.Tk()
janela.geometry("500x300")
Application(janela)
janela.mainloop()