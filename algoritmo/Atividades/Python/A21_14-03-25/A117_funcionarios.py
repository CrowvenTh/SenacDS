class Funcinonario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario

    def ExibirInformacoes(self):
        print(f"Informações do funcionário: ")
        print(f"Nome: {self.getNome()}")
        print(f"Cargo: {self.getCargo()}")
        print(f"Salário: R${self.getSalario()}")
    
    def CalcularBonus(self):
        bonus = self.getSalario() / 10
        print(f"Bônus salarial: R${bonus}")
#==============================================
class Gerente(Funcinonario):
    def __init__(self, nome, cargo, salario, setor):
        super().__init__(nome, cargo, salario)
        self.__setor = setor

    def getSetor(self):
        return self.__setor
    
    def setSetor(self, setor):
        self.__setor = setor

    def ExibirInformacoes(self):
        super().ExibirInformacoes()
        print(f"Setor: {self.getSetor()}")

funcinonario = Gerente("Thiago", "Desenvolvedor Jr", 8500, "Backend")
funcinonario.ExibirInformacoes()
funcinonario.CalcularBonus()