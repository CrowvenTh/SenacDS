class Banco:
    def __init__(self):
        self.__titular = None
        self.__saldo = 0.0
        self.__deposito = 0.0
        self.__saque = 0.0

    def getTitular(self):
        return self.__titular
    
    def getSaldo(self):
        return self.__saldo
    
    def getDeposito(self):
        return self.__deposito
    
    def getSaque(self):
        return self.__saque
    
    def setTitular(self, titular):
        self.__titular = titular
    
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def setDeposito(self, deposito):
        self.__deposito = deposito
    
    def setSaque(self, saque):
        self.__saque = saque

    def Salvatitular(self):
        self.titular = str(input("Insira o nome do titular: ")).capitalize()
        self.setTitular(self.titular)

    def ExibeDados(self):
        print(f"Titular: {self.getTitular()}")
        print(f"Saldo: R${self.getSaldo():.2f}")

    def Depositar(self):
        self.deposito = float(input("insira o valor do depósito: "))
        self.setDeposito(self.deposito)
        novoSaldo = self.getSaldo() + self.getDeposito()
        self.setSaldo(novoSaldo)
        print(f"Depósito de R${self.getDeposito():.2f} realizado com sucesso!")

    def Sacar(self):
        self.saque = float(input("Insira o valor do saque: "))
        if(self.saque > self.getSaldo()):
            print("Saldo Insuficiente!")
        else:
            self.setSaque(self.saque)
            novosaldo = self.getSaldo() - self.getSaque()
            self.setSaldo(novosaldo)
            print(f"Saque de R${self.getSaque():.2f} realizado com sucesso!")

    def Entrada(self):
        print("\n=====| BANCO |=====")
    
    def Menu(self):
        print("""
=====| MENU |=====
| 1 - Depositar
| 2 - Sacar
| 3 - Saldo 
| 4 - Encerrar
""")
        opcao = int(input("Insira um opção: "))
        while True:
            match opcao:
                case 1:
                    self.Depositar()
                    self.Menu()
                case 2:
                    self.Sacar()
                    self.Menu()
                case 3:
                    self.ExibeDados()
                    self.Menu()
                case 4:
                    print("programa encerrado")
                    break
                case _:
                    print("Opção Inválida!")
                    self.Menu()
                
    def OrganizaMenu(self):
        conta.Entrada()
        conta.Salvatitular()
        conta.Menu()

conta = Banco()
conta.OrganizaMenu()
    