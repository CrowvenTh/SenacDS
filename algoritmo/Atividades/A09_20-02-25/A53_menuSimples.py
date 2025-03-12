# Crie um programa que solicite ao usuário para digitar uma palavra. O programa deve continuar solicitando palavras até que o usuário digite a palavra "sair", momento em que o programa deve exibir uma mensagem de despedida e encerrar.

while True:
    palavra = input("Digite uma palavra ou 'sair' para encerrar o programa: ")
    if(palavra == "sair"):
        print("Programa encerrado...")
        break
