class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, saldo):
        self.__saldo = saldo

    def Deposito(self, valor):
        self.__saldo += valor
        print(f"Depósito de R${valor} realizado!")
    
    def Saque(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado")
        else:
            print(f"Saque de R${valor} negado, saldo insuficiente!")

    def ExibirSaldo(self):
        print(f"Saldo atual: R${self.getSaldo()}")

# conta = ContaBancaria("Thiago", 0)
# conta.Deposito(500)
# conta.ExibirSaldo()
# conta.Saque(250)
# conta.ExibirSaldo()
