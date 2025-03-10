class Livraria:
    def __init__(self):
        self.livraria = []

    def AdicionarLivro(self, livro):
        self.livro = livro
        self.livraria.append(self.livro)
    
    def ListaLivros(self):
        for i, self.livro in enumerate(self.livraria, 1):
            print(f"{i} - {self.livro}")

livraria1 = Livraria()
livraria1.AdicionarLivro("The witcher")
livraria1.AdicionarLivro("Crônicas do Gelo & Fogo")
livraria1.AdicionarLivro("Gigantes da física")
livraria1.ListaLivros() 