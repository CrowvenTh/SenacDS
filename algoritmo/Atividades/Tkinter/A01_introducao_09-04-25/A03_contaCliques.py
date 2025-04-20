import tkinter as tk

def Ola():
    label_ola = tk.Label(janela, text = "Olá, mundo!")
    label_ola.pack()

janela = tk.Tk()
janela.title("Janela de apresentação")

botao = tk.Button(janela, text="Clique aqui", command=Ola)

cont = 0
def contar():
    global cont
    cont += 1
    label_cont.config(text=f"Cliques: {cont}")

label_cont = tk.Label(janela, text="Cliques: 0")
label_cont.pack(pady = 10)

botao.pack()
janela.mainloop() 