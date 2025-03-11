class Inventario:
    def __init__(self):
        self.produtos = []

    def AdicionarProdutos(self, nome, qtd):
        self.nome = nome
        self.qtd = qtd
        self.produtos.append({"Nome":nome, "Quantidade":qtd})

    def ListarProdutos(self):
        for i,self.produtos in enumerate(self.produtos, 1):
            # print(f"ID {i} | Nome: {self.nome} | Quantidade: {self.qtd}")
            nomes = self.produtos["Nome"]
            qtds = self.produtos["Quantidade"]
            print(f"ID {i} | Nome: {nomes} | Quantidade: {qtds}")
def Inicia():
    print("\n=======| INVENTÁRIO |=======")

estoque = Inventario()
Inicia()
estoque.AdicionarProdutos("Caixote", "50")
estoque.AdicionarProdutos("Ferragem", "80")
estoque.AdicionarProdutos("Vergalhão", "40")
estoque.AdicionarProdutos("Cimento", "60")
estoque.AdicionarProdutos("Tijolo", "250")
estoque.ListarProdutos()