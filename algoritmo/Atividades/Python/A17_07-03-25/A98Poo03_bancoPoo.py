class Banco:
    saldo = 0
    def __init__(self):
        self
    
    def Titular(self):
        self.titular = input("Insira o nome do titular: ").capitalize()

    def MostrarSaldo(self):
        print(f"===| Titular: {self.titular}\n===| Saldo atual: R${self.saldo}\n")

    def DepositarValor(self):
        self.deposito = float(input("===| Insira o valor do deposito: "))
        self.saldo += self.deposito
        print(f"===| Titular: {self.titular}\n===| Depósito de R${self.deposito} realizado com sucesso!\n")
    
    def SacarValor(self):
        self.saque = float(input("===| Insira o valor do saque: "))
        if(self.saldo > self.saque):
            self.saldo -= self.saque
            print(f"===| Titular: {self.titular}\n===| Saque de R${self.saque} realizado com sucesso!\n")
        else: 
            print(f"===| Titular: {self.titular}\n===| Saque de R${self.saque} negado!\n===| Saldo Insuficiente.\n")
            
def main():
    conta = Banco()
    conta.Titular()
    conta.MostrarSaldo()
    conta.DepositarValor()
    conta.MostrarSaldo()
    conta.SacarValor()
    conta.MostrarSaldo()

main()