# Escreva um programa que solicite ao usuário que insira números e calcule a soma desses números até que a soma ultrapasse um limite específico, usando um loop while
on = True
somaIterada = 0
limite = int(input("Insira um resultado limite: "))
while on:
    numero = int(input("Insira um número: "))
    numero1 = int(input("Insira outro número: "))
    soma = (numero + numero1)
    somaIterada += soma
    if(somaIterada < limite):
            print(f"{somaIterada} | {limite}")
    if(somaIterada > limite):
        print(f"{somaIterada} | {limite}")
        on = False
    