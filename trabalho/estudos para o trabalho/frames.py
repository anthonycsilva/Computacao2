from tkinter import*
from tkinter import messagebox
from tkinter import filedialog

principal = Tk()
principal.title('<<<<LOGO FODA')
principal.iconbitmap('D:/Users/antho/Documents/Python Stuff/comp2/trabalho/principal/imagens/logoicon.ico')

quadrante = LabelFrame(principal, text ="Quadrante foda...", padx=5,pady=5)
quadrante.pack(padx=10, pady=10)


numero = StringVar()





def clicado1():
    frase = Label(quadrante, text='BESTO FRENDO')
    frase.pack()


def clicado2():
    frase = Label(quadrante, text='ESTOU DECEPCIONADO')
    frase.pack()


def popupFoda():
    messagebox.showinfo('ALO CARALHO', 'OLÁ MUNDO')

def selecionaCaminho():
    caminho = filedialog.askdirectory()
    global localizacao
    localizacao = caminho
    Label(quadrante, text=caminho).pack()


botao_caminho = Button(quadrante, text='Selecione a pasta que deseja ', command=selecionaCaminho)


frase = Label(quadrante, text='Qual tipo de mulher vc prefere??').pack()
botao1 = Button(quadrante, text='Alta e com Bunda Grande', command=clicado1).pack()
botao2 = Button(quadrante, text='Qualquer outro tipo', command=clicado2).pack()
principal.mainloop()