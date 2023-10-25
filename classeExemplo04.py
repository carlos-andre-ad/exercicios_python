from tkinter import *



class Application:
    def __init__(self, master=None):
        janela.title("Telas Frames")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg = Label(self.tela1, text="Hello Wordl 1")
        self.msg.pack()
        self.botao = Button(self.tela1, text="Fechar",command=self.tela1.quit)
        self.botao.pack()
        self.tela2 = Frame(master)
        self.tela2.pack()
        self.msg = Label(self.tela2, text="Hello Wordl 2")
        self.msg.pack()
        self.botao = Button(self.tela2, text="Cancelar", command=self.tela2.quit)
        self.botao.pack()
        
        
janela = Tk()
janela.geometry("500x300")
Application(janela)
janela.mainloop()

