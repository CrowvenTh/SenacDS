# Escreva um programa que solicite ao usuário que insira uma senha correta e continue pedindo até que a senha correta seja inserida, usando um loop while.

senha = input("Cadastre sua senha: ")
userSenha = input("Digite sua senha: ")

while True:
    if(senha != userSenha):
        print("Senha incorreta!")
        userSenha = input("Digite sua senha: ")
    else: 
        print("Senha Correta!")
        break

    