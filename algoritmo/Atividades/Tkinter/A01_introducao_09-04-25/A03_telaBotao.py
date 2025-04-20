import tkinter as tk

def Ola():
    print("Bem Vindo(a)!")

janela = tk.Tk()
janela.title("Janela com botão")

botao = tk.Button(
    janela,
    text = "Clique aqui",
    command = Ola
)

botao.pack()
janela.mainloop()
