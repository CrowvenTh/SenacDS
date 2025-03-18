# Escreva um programa que conte de 1 a 10 usando um loop while e imprima cada número.

contador = 0
while contador < 10:
    contador += 1 # nessa posição o contador vai do 10 ao 1
    print(contador)
    # contador += 1 nessa posição o contador vai do 0 ao 9

# OU
    
for i in range(1, 11, +1):
    print(i)