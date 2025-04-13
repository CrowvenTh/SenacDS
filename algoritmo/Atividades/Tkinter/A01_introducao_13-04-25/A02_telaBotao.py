import tkinter as tk

def Ola():
    print("Olá, mundo!")

janela = tk.Tk()
janela.title("Janela com botão")

botao = tk.Button(
    janela,
    text = "Bem vindo(a)!",
    command = Ola
)

botao.pack()
janela.mainloop()
