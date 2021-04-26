from tkinter import*
from tkinter import messagebox
from tkinter import filedialog

principal = Tk()

quadrante = LabelFrame(principal, text ="Quadrante foda...", padx=5,pady=5)
quadrante.pack(padx=10, pady=10)


numero = StringVar()


def clicado(valor):
    frase = Label(quadrante, text=numero.get())
    frase.pack()


def popupFoda():
    messagebox.showinfo('ALO CARALHO', 'OLÁ MUNDO')

def selecionaCaminho():
    caminho = filedialog.askdirectory()
    global localizacao
    localizacao = caminho
    Label(quadrante, text=caminho).pack()


botao_caminho = Button(quadrante, text='Selecione a pasta que deseja ', command=selecionaCaminho).pack()


frase = Label(quadrante, text='Quem é vc??').pack()
Radiobutton(quadrante, text='Eu Jogo Potemkin', variable=numero, value='Besto Friendo', command=lambda: clicado(numero.get())).pack()
Radiobutton(quadrante, text='Eu jogo de Jack-O', variable=numero, value='Deve ser mt triste viver sozinho, continue assim', command=lambda: clicado(numero.get())).pack()

principal.mainloop()