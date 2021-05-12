from tkinter import*

principal = Tk()
principal.title('Calculadora Simples')
tela = Entry(principal, width=50)
tela.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)

def clique_botao(numero):
    atual = tela.get()
    tela.delete(0,END)
    tela.insert(0, str(atual) + str(numero))

def clique_limpar():
    tela.delete(0, END)

def clique_somar():
    primeiro_numero = int(tela.get())
    global numero1 
    numero1 = primeiro_numero
    tela.delete(0,END)

def clique_resultado():
    resultado = numero1 + int(tela.get())
    tela.delete(0,END)
    tela.insert(0, resultado)

#definindo botão

numero_1 = Button(principal, text='1', padx=40, pady = 20, command=lambda: clique_botao(1))
numero_2 = Button(principal, text='2', padx=40, pady = 20, command=lambda: clique_botao(2))
numero_3 = Button(principal, text='3', padx=40, pady = 20, command=lambda: clique_botao(3))
numero_4 = Button(principal, text='4', padx=40, pady = 20, command=lambda: clique_botao(4))
numero_5 = Button(principal, text='5', padx=40, pady = 20, command=lambda: clique_botao(5))
numero_6 = Button(principal, text='6', padx=40, pady = 20, command=lambda: clique_botao(6))
numero_7 = Button(principal, text='7', padx=40, pady = 20, command=lambda: clique_botao(7))
numero_8 = Button(principal, text='8', padx=40, pady = 20, command=lambda: clique_botao(8))
numero_9 = Button(principal, text='9', padx=40, pady = 20, command=lambda: clique_botao(9))
numero_0 = Button(principal, text='0', padx=40, pady = 20, command=lambda: clique_botao(0))
botao_soma = Button(principal, text='+', padx=39, pady=20, command=clique_somar)
botao_resultado = Button(principal, text='=', padx=91, pady=20, command=clique_resultado)
botao_limpar = Button(principal, text='Limpar', padx=76, pady=20, command=clique_limpar)

#layout dos botão tudo
numero_1.grid(row=3, column=0)
numero_2.grid(row=3, column=1)
numero_3.grid(row=3, column=2)

numero_4.grid(row=2, column=0)
numero_5.grid(row=2, column=1)
numero_6.grid(row=2, column=2)

numero_7.grid(row=1, column=2)
numero_8.grid(row=1, column=1)
numero_9.grid(row=1, column=0)

numero_0.grid(row=4, column=0)
botao_limpar.grid(row=4, column=1, columnspan=2)
botao_soma.grid(row=5, column=0)
botao_resultado.grid(row=5, column=1, columnspan=2)




principal.mainloop()

