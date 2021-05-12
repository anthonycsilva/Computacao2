from tkinter import*
from tkinter import filedialog

principal = Tk()
principal.title('Organizer')
principal.iconbitmap('D:/Users/antho/Documents/Python Stuff/comp2/trabalho/principal/imagens/logoicon.ico')

quadrante = LabelFrame(principal, padx=10,pady=10)
quadrante.grid(row =10, column=10)

titulo= Label(quadrante, text='---Organizer---').grid(row=0, column=2)

#metodos:

def selecionaCaminho():
    caminho = filedialog.askdirectory()
    global localizacao
    localizacao = caminho
    #depositLabel = Label(self, textvariable=labelText)
    Label(quadrante,text=f'Pasta Selecionada: {caminho}').grid(row=3, column=2)


frase_selecione = Label(quadrante, text='Selecione a pasta que você deseja organizar:').grid(row=1, column=2)
botao_seleciona_pasta = Button(quadrante, text='Selecione...', width=30, command=selecionaCaminho).grid(row=2, column=2)
#pastas
Label(quadrante, text='----------------------------//----------------------------').grid(row=6, column=2)
selecione_nome_pasta = Label(quadrante, text='Escolha o nome de suas pastas:').grid(row=7, column=2)

#executaveis

Label(quadrante, text='Executáveis:').grid(row=8, column=1)
tela1 = Entry(quadrante, width=15).grid(row=8, column=3)

#executaveis

Label(quadrante, text='PDF:').grid(row=9, column=1)
tela1 = Entry(quadrante, width=15).grid(row=9, column=3)

#executaveis

Label(quadrante, text='Compactados').grid(row=10, column=1)
tela1 = Entry(quadrante, width=15).grid(row=10, column=3)

#executaveis

Label(quadrante, text='Imagens').grid(row=11, column=1)
tela1 = Entry(quadrante, width=15).grid(row=11, column=3)

#executaveis

Label(quadrante, text='Videos').grid(row=12, column=1)
tela1 = Entry(quadrante, width=15).grid(row=12, column=3)

#executaveis

Label(quadrante, text='Musicas').grid(row=13, column=1)
tela1 = Entry(quadrante, width=15).grid(row=13, column=3)

#executaveis

Label(quadrante, text='Textos').grid(row=14, column=1)
tela1 = Entry(quadrante, width=15).grid(row=14, column=3)

#executaveis

Label(quadrante, text='Planilhas').grid(row=15, column=1)
tela1 = Entry(quadrante, width=15).grid(row=15, column=3)

#executaveis

Label(quadrante, text='Slides PowerPoint').grid(row=16, column=1)
tela1 = Entry(quadrante, width=15).grid(row=16, column=3)

#executaveis

Label(quadrante, text='Extras').grid(row=17, column=1)
tela1 = Entry(quadrante, width=15).grid(row=17, column=3)


#botão master

botao_master = Button(quadrante, text='Organizar', width=30).grid(row=18, column=2)

principal.mainloop()