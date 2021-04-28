from tkinter import*
from tkinter import filedialog
import os
import shutil

principal = Tk()
principal.title('Organizer')
principal.iconbitmap('D:/Users/antho/Documents/Python Stuff/comp2/trabalho/principal/imagens/logoicon.ico')

quadrante = LabelFrame(principal, padx=10,pady=10)
quadrante.grid(row =10, column=10)

titulo= Label(quadrante, text='---Organizer---').grid(row=0, column=2)

#pastas
Label(quadrante, text='----------------------------//----------------------------').grid(row=6, column=2)
selecione_nome_pasta = Label(quadrante, text='Escolha o nome de suas pastas:').grid(row=7, column=2)

#executaveis

Label(quadrante, text='Executáveis:').grid(row=8, column=1)
tela1 = Entry(quadrante, width=15)
tela1.grid(row=8, column=3)

#executaveis

Label(quadrante, text='PDF:').grid(row=9, column=1)
tela2 = Entry(quadrante, width=15)
tela2.grid(row=9, column=3)

#executaveis

Label(quadrante, text='Compactados').grid(row=10, column=1)
tela3 = Entry(quadrante, width=15)
tela3.grid(row=10, column=3)

#executaveis

Label(quadrante, text='Imagens').grid(row=11, column=1)
tela4 = Entry(quadrante, width=15)
tela4.grid(row=11, column=3)

#executaveis

Label(quadrante, text='Videos').grid(row=12, column=1)
tela5 = Entry(quadrante, width=15)
tela5.grid(row=12, column=3)

#executaveis

Label(quadrante, text='Musicas').grid(row=13, column=1)
tela6 = Entry(quadrante, width=15)
tela6.grid(row=13, column=3)

#executaveis

Label(quadrante, text='Textos').grid(row=14, column=1)
tela7 = Entry(quadrante, width=15)
tela7.grid(row=14, column=3)

#executaveis

Label(quadrante, text='Planilhas').grid(row=15, column=1)
tela8 = Entry(quadrante, width=15)
tela8.grid(row=15, column=3)

#executaveis

Label(quadrante, text='Slides PowerPoint').grid(row=16, column=1)
tela9 = Entry(quadrante, width=15)
tela9.grid(row=16, column=3)

#executaveis

Label(quadrante, text='Extras').grid(row=17, column=1)
tela10 = Entry(quadrante, width=15)
tela10.grid(row=17, column=3)

#metodos:

def selecionaCaminho():
    caminho = filedialog.askdirectory()
    global localizacao
    localizacao = caminho
    #depositLabel = Label(self, textvariable=labelText)
    Label(quadrante,text=f'Pasta Selecionada: {caminho}').grid(row=3, column=2)

def pegar_extensao(nome):
    index = nome.rfind('.')
    #rfind no Python retorna a posição da última ocorrência da cadeia, se não houver correspondência -1 é retornado
    #selecionando apenas as posições após o ponto você consegue saber que tipo é o arquivo
    return nome[index:]


def organizador():
    pasta = localizacao
    #Aqui eu configuro quais tipos de extenções serão reconhecidas pelo programa
    exec_ext = ['.exe','.msi']
    pdf_ext = ['.pdf']
    img_ext = ['.jpg', '.jpeg', '.png']
    vid_ext = ['.mp4', '.avi','.wmv','.mkv']
    zip_ext = ['.rar', '.zip','.7z']
    musica_ext = ['.mp3']
    doc_ext = ['.doc', '.docx','.txt']
    planilha_ext = ['.xls','.xlt','.xml']
    pp_ext = ['.ppt','.pps']


    EXEC_DIR = os.path.join(pasta, tela1.get())
    PDF_DIR = os.path.join(pasta, tela2.get())
    IMG_DIR = os.path.join(pasta, tela3.get())
    VID_DIR = os.path.join(pasta, tela4.get())
    MU_DIR = os.path.join(pasta, tela5.get())
    ZIP_DIR = os.path.join(pasta, tela6.get())
    DOC_DIR = os.path.join(pasta, tela7.get())
    PLA_DIR = os.path.join(pasta, tela8.get())
    PP_DIR = os.path.join(pasta, tela9.get())
    ETC_DIR = os.path.join(pasta, tela10.get())

    if not os.path.isdir(EXEC_DIR):
        os.mkdir(EXEC_DIR)
    if not os.path.isdir(PDF_DIR):
        os.mkdir(PDF_DIR)
    if not os.path.isdir(IMG_DIR):
        os.mkdir(IMG_DIR)
    if not os.path.isdir(VID_DIR):
        os.mkdir(VID_DIR)
    if not os.path.isdir(MU_DIR):
        os.mkdir(MU_DIR)
    if not os.path.isdir(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    if not os.path.isdir(DOC_DIR):
        os.mkdir(DOC_DIR)
    if not os.path.isdir(PLA_DIR):
        os.mkdir(PLA_DIR)
    if not os.path.isdir(PP_DIR):
        os.mkdir(PP_DIR)
    if not os.path.isdir(ETC_DIR):
        os.mkdir(ETC_DIR)


    arquivos = os.listdir(pasta)
    nova_pasta = ''
    #if os.path.isfile(os.path.join(diretorio, arquivo)):
    for i in arquivos:
        if os.path.isfile(os.path.join(pasta, i)):
            extensao = str.lower(pegar_extensao(i))
            if extensao in exec_ext:
                nova_pasta = EXEC_DIR
            elif extensao in pdf_ext:
                nova_pasta = PDF_DIR
            elif extensao in img_ext:
                nova_pasta = IMG_DIR
            elif extensao in vid_ext:
                nova_pasta = VID_DIR
            elif extensao in zip_ext:
                nova_pasta = ZIP_DIR
            elif extensao in doc_ext:
                nova_pasta = DOC_DIR
            elif extensao in musica_ext:
                nova_pasta = MU_DIR
            elif extensao in planilha_ext:
                nova_pasta = PLA_DIR
            elif extensao in pp_ext:
                nova_pasta = PP_DIR
            else:
                nova_pasta = ETC_DIR
            
            shutil.move(os.path.join(pasta, i), os.path.join(nova_pasta, i))   
            print(f'Arquivo: {i}, movido para: {os.path.join(nova_pasta,i)}')


frase_selecione = Label(quadrante, text='Selecione a pasta que você deseja organizar:').grid(row=1, column=2)
botao_seleciona_pasta = Button(quadrante, text='Selecione...', width=30, command=selecionaCaminho).grid(row=2, column=2)


#botão master

botao_master = Button(quadrante, text='Organizar', width=30, command=organizador).grid(row=18, column=2)

principal.mainloop()

