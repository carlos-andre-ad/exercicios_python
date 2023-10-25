import tkinter as tk
from tkinter import ttk



janela = tk.Tk()
janela.title('Usando Combobox')
janela.geometry('400x250')


ttk.Label(janela, text = "Exemplo de Combobox Widget", background='red', foreground ="black", font=("Times New Roman",15)).grid(row = 0,column = 1)

ttk.Label(janela, text = "Selecione um mês :", font=("Times New Roman",12)).grid(column=0,row=5,padx=10,pady=25)


n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)
escolha['values'] = (' Janeiro',
                    ' Fevereiro',
                    ' Março',
                    ' Abril',
                    ' Maio',
                    ' Junho',
                    ' Julho',
                    ' Agosto',
                    ' Setembro',
                    ' Outubro',
                    ' Novembro',
                    ' Dezembro')
escolha.grid(column = 1, row = 5)
escolha.current()
janela.mainloop()