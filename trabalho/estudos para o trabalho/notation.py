from tkinter import *

principal = Tk()



def soma(n):
    Label(principal, text=f'Soma + 1: {n+1}').pack()


frase = Label(principal, text='Clara Legal')
frase.pack()

a = Entry(principal)
a.pack()


botao= Button(principal, text='Clique aqui', command=lambda:soma(4))
botao.pack()


botao2= Button(principal, text='Clique aqui', command=lambda:soma(4))
botao2.pack()

botao3= Button(principal, text='Clique aqui', command=lambda:soma(4))
botao3.pack()

botao4= Button(principal, text='Clique aqui', command=lambda:soma(4))
botao4.pack()
principal.mainloop()
