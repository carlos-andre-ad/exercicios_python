import tkinter as tk


def escolhe_linguag():
    escolha = v.get()
    if escolha == 1:
         print("A linguagem escolhido foi PHP!")
    elif escolha == 2:
         print("A linguagem escolhido foi DotNet!")
    else:
         print("A linguagem escolhido foi Java!")

janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,
text="Escolha uma linguagem de programação:",justify = tk.LEFT,padx = 20).pack()
tk.Radiobutton(janela,text="Python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
tk.Radiobutton(janela,text="Java",padx = 25,variable=v,value=3).pack(anchor=tk.W)
tk.Button(janela, text='Imprime escolha', command=escolhe_linguag).pack()


janela.geometry("500x300")
janela.mainloop()

