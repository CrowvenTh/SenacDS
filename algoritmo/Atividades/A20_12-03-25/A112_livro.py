class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.__preco = preco

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco

    def ExibirPreco(self):
        print(f"Título: {self.titulo}\nPreço: R${self.getPreco()}")

livro1 = Livro("The Witcher", 132.95)
livro1.ExibirPreco()