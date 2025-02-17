print("--------------------\n-----| Banco | -----\n--------------------")
print("| Selecione uma opção:\n| 0 - Encerrar programa \n| 1 - Realizar depósito \n| 2 - Realizar Saque \n| 3 - Verificar Saldo\n--------------------\n")
def menu():
    print("| Selecione uma opção:\n| 0 - Encerrar programa \n| 1 - Realizar depósito \n| 2 - Realizar Saque \n| 3 - Verificar Saldo\n--------------------\n")

print(menu())
opcao = int(input(": "))
while opcao != 0:
        if(opcao == 1):
            deposito = float(input("| Insira o valor do depósito: "))
            saldo += deposito
            print(f"| Depósito de R${deposito} realizado com sucesso!\n")
            print(menu())
            opcao = int(input(": "))
        elif(opcao == 2):
            saque = float(input("| Insira o valor do saque: "))
            saque -= saldo
            if(saque > saldo):
                print("| Saldo insuficiente.")
                print(menu())
                opcao = int(input(": "))
            else:
                print(f"| Saque de R${saque} realizado com sucesso!\n")
                print(menu())
                opcao = int(input(": "))
        elif(opcao == 3):
            print(f"| Saldo atual: R${saldo}")
            print(menu())
            opcao = int(input(": "))
        else:
            print("| Programa encerrado.\n")
            opcao == 0
