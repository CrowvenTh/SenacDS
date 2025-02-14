contaCorrente = 0.0
print("--------------------\n-----| Banco | -----\n--------------------")
print("| Selecione uma opção:\n| 0 - Encerrar programa \n| 1 - Realizar depósito \n| 2 - Realizar Saque \n| 3 - Verificar Saldo\n--------------------\n")

def menu():
    print("| Selecione uma opção:\n| 0 - Encerrar programa \n| 1 - Realizar depósito \n| 2 - Realizar Saque \n| 3 - Verificar Saldo\n--------------------\n")


print(menu())
opcao = int(input(": "))
while opcao != 0:
        if(opcao == 1):
            deposito = float(input("| Insira o valor do depósito: "))
            deposito += contaCorrente
            print(f"| Depósito de R${deposito} realizado com sucesso!")
            print(menu())
            opcao = int(input(": "))
        elif(opcao == 2):
            saque = float(input("| Insira o valor do saque: "))
            saque -= contaCorrente
            if(saque > contaCorrente):
                print("| Saldo insuficiente.")
                print(menu())
                opcao = int(input(": "))
            else:
                print(f"| Saque de R${saque} realizado com sucesso!")
                print(menu())
                opcao = int(input(": "))
        elif(opcao == 3):
            print(f"| Saldo atual: R${contaCorrente}")
            print(menu())
            opcao = int(input(": "))
        else:
            print("| Programa encerrado.")
            opcao == 0
