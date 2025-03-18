class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        # self.valor = valor

    def Depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("deposito realizado")
        else: 
            print("valro inválido")

    def Sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print("saque realizado")

    def ExibirSaldo(self):
        print(f"Saldo atual: {self.saldo}")

# conta = ContaBancaria("Thiago", 0)
# conta.Depositar(150)
# conta.ExibirSaldo()
# conta.Sacar(50)
# conta.ExibirSaldo()