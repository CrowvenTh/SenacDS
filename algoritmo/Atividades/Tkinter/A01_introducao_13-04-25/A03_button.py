import tkinter as tk

def Ola():
    label_ola = tk.Label(janela, text = "Olá, mundo!")
    label_ola.pack()

janela = tk.Tk()
janela.title("Olá mundo na janela")

botao = tk.Button(janela, text = "Clique aqui",
                  command=Ola)
botao.pack()

janela.mainloop()