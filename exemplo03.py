import tkinter


janela = tkinter.Tk()
janela.title("Trabalhando GUI em Python")
botao = tkinter.Button(janela,text="OLÁ")
botao.pack()
janela.geometry("500x300")
janela.mainloop()