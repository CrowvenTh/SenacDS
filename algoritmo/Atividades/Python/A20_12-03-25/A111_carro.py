class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.__ano = ano

    def getAno(self):
        return self.__ano
     
    def setAno(self, ano):
        self.__ano = ano

    def ExibirAno(self):
        print(f"Ano do carro: {self.getAno()}")

carro1 = Carro("Type R", 2020)
carro1.ExibirAno()
carro1.getAno()