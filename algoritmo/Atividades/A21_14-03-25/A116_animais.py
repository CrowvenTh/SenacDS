class Animal:
    def __init__(self, especie, nome, idade):
        self.especie = (especie)
        self.nome = nome
        self.idade = idade

    def getEspecie(self):
        return self.especie
    
    def setEspecia(self, especie):
        self.especie = especie

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade

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