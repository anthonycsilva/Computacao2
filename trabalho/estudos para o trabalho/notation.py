from tkinter import *

root = Tk()


e = Entry(root,width = 50)
e.get() # recebe o que foi escrito na Entry
e.insert(0, "Digite Algo: ") # Insere um valor pré determinado na Entry

def cliquesx():
    frase_botao = Label(root, text = f'Olá: {e.get()}')
    frase_botao.pack()

frase = Label(root, text='Vitória de Boné').pack()
e.pack()
botao = Button(root, text="Clique aqui",command = cliquesx).pack()

root.mainloop()
