class Animal:
    def __init__(self, especie, nome, idade):
        self.__especie = (especie)
        self.__nome = nome
        self.__idade = idade

    def getEspecie(self):
        return self.__especie
    
    def setEspecia(self, especie):
        self.__especie = especie

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        self.__idade = idade

    def EmitirSom(self):
        print(f"{self.getNome} está emitindo latindo!!!")

    def Infomracoes(self):
        print(f"Informações do animal")
        print(f"Espécie: {self.getEspecie()}")
        print(f"Nome: {self.getNome()}")
        print(f"Idade: {self.getIdade()} anos")
        #================================================

class Cachorro(Animal):
    def AbanarRabo(self):
        print(f"O {self.getNome()} está abanandoo rabo!!!")

perro = Cachorro("Cachorro","Chase",8)
perro.EmitirSom()
perro.Infomracoes()
perro.AbanarRabo()