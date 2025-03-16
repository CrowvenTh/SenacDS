from A118_smartphone import Dispositivo

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, preco, so):
        super().__init__(marca, modelo, preco)
        self.__so = so

    def getSo(self):
            return self.__so

    def setSo(self, so):
            self.__so = so

    def ExibirDados(self):
        super().ExibirDados()
        print(f"Sistema Operacional: {self.getSo()}\n")

celular1 = Smartphone("Samsung", "Galaxy S24", 7500, "Android")
celular2 = Smartphone("Apple", "Iphone 16", 12500, "IOS")

celular1.ExibirDados()
celular2.ExibirDados()