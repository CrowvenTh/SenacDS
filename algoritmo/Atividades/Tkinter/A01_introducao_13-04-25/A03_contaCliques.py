import tkinter as tk

cont = 0
def ContaClique():
    global cont
    cont += 1
    label_cont.config(text=f"Cliques: {cont}")

janela = tk.Tk()
janela.title("Window")
janela.mainloop()
label_cont = tk.Label(janela, text="Cliques: 0")
label_cont.pack(pady=10)
