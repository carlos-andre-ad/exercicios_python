import tkinter


janela = tkinter.Tk()
janela.title("Botões c/ Método pack()")
botao = tkinter.Button(janela,text="Alinhado a esquerda",fg="red").pack(side= "left")
janela.geometry("500x300")
janela.mainloop()