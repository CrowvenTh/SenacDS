class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = estoque

    def vender(self,qtd):
        self.qtd = qtd
        if (self.estoque > qtd and qtd > 0):
            self.estoque -= qtd
            print(f"Estoque atual: {self.estoque}")
        else:
            print("Valor inválido")

book = Livro("The Witcher","Andrzej Sapkowski",150)
book.vender(50)
        
# OU

class Livro:
    def __init__(self):
        self.titulo = input("Insira o Titulo: ")
        self.autor = input("Insira o Autor: ")
        self.estoque = int(input("Insira o Estoque: " ))

    def vender(self):
        qtd = int(input("Insira a qtd a vender: "))
        if (self.estoque > qtd and qtd > 0):
            self.estoque -= qtd
            print(f"Estoque atual: {self.estoque}")
        else: 
            print("valor inválido")

book = Livro()
book.vender()