# Escreva um programa em Python que solicite ao usuário informações sobre uma data (dia, mês e ano) e utilize o parâmetro sep na função print() para imprimir a data no formato "DD/MM/AAAA".

day = int(input("Insira o dia: "))
month = int(input("Insira o mês: "))
year = int(input("Insira o ano: "))

print(day, month, year, sep="/")
