import os
import shutil

def pegar_extensao(nome):
    index = nome.rfind('.')
    #rfind no Python retorna a posição da última ocorrência da cadeia, se não houver correspondência -1 é retornado
    #selecionando apenas as posições após o ponto você consegue saber que tipo é o arquivo
    return nome[index:]


def organizador():
    pasta = str(input('Digite a localização da sua pasta de Download: '))
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


    EXEC_DIR = os.path.join(pasta, 'Executáveis')
    PDF_DIR = os.path.join(pasta, 'Arquivos PDF')
    IMG_DIR = os.path.join(pasta, 'Imagens')
    VID_DIR = os.path.join(pasta, 'Videos')
    MU_DIR = os.path.join(pasta,'Musicas')
    ZIP_DIR = os.path.join(pasta, 'Arquivos Zipados')
    DOC_DIR = os.path.join(pasta, 'Documentos de Texto')
    PLA_DIR = os.path.join(pasta, 'Planilhas')
    PP_DIR = os.path.join(pasta, 'Power Point')
    ETC_DIR = os.path.join(pasta, 'Outros')

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

organizador()