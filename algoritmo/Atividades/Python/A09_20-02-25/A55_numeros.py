# Crie um programa que peça ao usuário para digitar números até que ele digite um número negativo. Em seguida, imprima a soma dos números digitados.

total = 0
while True:
    numero = int(input("Ínsira os números: "))
    if(numero > 0):
        total += numero
    else:
        print(f"A soma dos números digitados é igual a: {total}")
        break
