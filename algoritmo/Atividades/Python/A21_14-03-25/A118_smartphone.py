class Dispositivo:
    def __init__(self, marca, modelo, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPreco(self):
        return self.__preco
    
    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setPreco(self, preco):
        self.__preco = preco

    def ExibirDados(self):
        print(f"Informações do aparelho:")
        print(f"Marca: {self.getMarca()}")
        print(f"Modelo: {self.getModelo()} ")
        print(f"Preço: R${self.getPreco()}")

aparelho1 = Dispositivo("Samsung", "S24", 6500)
aparelho2 = Dispositivo("Apple", "Iphone 16", 9450)

aparelho1.ExibirDados()
aparelho2.ExibirDados()